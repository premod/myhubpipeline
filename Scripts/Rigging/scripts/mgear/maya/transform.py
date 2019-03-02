# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10

"""
Functions to work with matrix and transformations.
"""


#############################################
# GLOBAL
#############################################
import math

from pymel import util as pmu
import pymel.core.datatypes as dt
import pymel.core.nodetypes as nt

import mgear.maya.vector as vec

#############################################
# TRANSFORM
#############################################
def getTranslation(node):
    """
    Return the position of the dagNode in worldSpace.

    Args:
        node (dagNode): The dagNode to get the translation

    Returns:
        matrix: The transformation matrix
    """
    return node.getTranslation(space="world")

def getTransform(node):
    """
    Return the transformation matrix of the dagNode in worldSpace.

    Args:
        node (dagNode): The dagNode to get the translation

    Returns:
        matrix: The transformation matrix
    """
    return node.getMatrix(worldSpace=True)

def getTransformLookingAt(pos, lookat, normal, axis="xy", negate=False):
    """
    Return the transformation matrix of the dagNode oriented looking to an specific point.

    Args:
        pos (vector): The position for the transformation
        lookat (vector): The aiming position to stablish the orientation.
        normal (vector): The normal control the transformation roll.
        axis (str): The 2 axis used for lookat and normal. Default "xy"
        negate (bool): If true, invert the aiming direction.

    Returns:
        matrix: The transformation matrix

    >>>  t = tra.getTransformLookingAt(self.guide.pos["heel"], self.guide.apos[-4], self.normal, "xz", self.negate)
    """

    normal.normalize()

    if negate:
        a = pos - lookat
    else:
        a = lookat - pos

    a.normalize()
    c = pmu.cross(a, normal)
    c.normalize()
    b = pmu.cross(c, a)
    b.normalize()

    if axis == "xy":
        X = a
        Y = b
        Z = c
    elif axis == "xz":
        X = a
        Z = b
        Y = -c
    elif axis == "yx":
        Y = a
        X = b
        Z = -c
    elif axis == "yz":
        Y = a
        Z = b
        X = c
    elif axis == "zx":
        Z = a
        X = b
        Y = c
    elif axis == "z-x":
        Z = a
        X = -b
        Y = -c
    elif axis == "zy":
        Z = a
        Y = b
        X = -c

    elif axis == "x-y":
        X = a
        Y = -b
        Z = -c
    elif axis == "-xz":
        X = -a
        Z = b
        Y = c
    elif axis == "-xy":
        X = -a
        Y = b
        Z = c

    m = dt.Matrix()
    m[0] = [X[0], X[1], X[2], 0.0]
    m[1] = [Y[0], Y[1], Y[2], 0.0]
    m[2] = [Z[0], Z[1], Z[2], 0.0]
    m[3] = [pos[0], pos[1], pos[2], 1.0]

    return m

def getChainTransform(positions, normal, negate=False):
    """
    Get a tranformation list from a positions list and normal.

    Args:
        positions(list of vector): List with the chain positions.
        normal (vector): Normal direction.
        negate (bool): If true invert the chain orientation.

    returns:
        list of matrix: The list containing the transformation matrix for the chain.

    >>> tra.getChainTransform(self.guide.apos, self.normal, self.negate)
    """

    # Draw
    transforms = []
    for i in range(len(positions)-1):
        v0 = positions[i-1]
        v1 = positions[i]
        v2 = positions[i+1]

        # Normal Offset
        if i > 0:
            normal = vec.getTransposedVector(normal, [v0, v1], [v1, v2])

        t = getTransformLookingAt(v1, v2, normal, "xz", negate)
        transforms.append(t)

    return transforms



def getChainTransform2(positions, normal, negate=False):
    """
    Get a tranformation list from a positions list and normal.

    Note:
        getChainTransform2 is using the latest position on the chain

    Args:
        positions(list of vector): List with the chain positions.
        normal (vector): Normal direction.
        negate (bool): If true invert the chain orientation.

    returns:
        list of matrix: The list containing the transformation matrix for the chain.

    >>> tra.getChainTransform2(self.guide.apos, self.normal, self.negate)
    """

    # Draw
    transforms = []
    for i in range(len(positions)):
        if i == len(positions)-1:
            v0 = positions[i-1]
            v1 = positions[i]
            v2 = positions[i-2]

        else:
            v0 = positions[i-1]
            v1 = positions[i]
            v2 = positions[i+1]

        # Normal Offset
        if i > 0 and i != len(positions)-1:
            normal = vec.getTransposedVector(normal, [v0, v1], [v1, v2])

        if i == len(positions)-1:
            t = getTransformLookingAt(v1, v0, normal, "-xz", negate)
        else:
            t = getTransformLookingAt(v1, v2, normal, "xz", negate)
        transforms.append(t)

    return transforms


def getTransformFromPos(pos):
    """
    Create a transformation Matrix from a given position.

    Args:
        pos (vector): Position for the transformation matrix

    Returns:
        matrix: The newly created transformation matrix

    >>>  t = tra.getTransformFromPos(self.guide.pos["root"])
    """

    m = dt.Matrix()
    m[0] = [1.0, 0, 0, 0.0]
    m[1] = [0, 1.0, 0, 0.0]
    m[2] = [0, 0, 1.0, 0.0]
    m[3] = [pos[0], pos[1], pos[2], 1.0]

    return m

def getOffsetPosition(node, offset=[0,0,0]):
    """
    Get an offset position from dagNode

    Args:
        node (dagNode): The dagNode with the original position.
        offset (list of float): Ofsset values for xyz. exp : [1.2, 4.6, 32.78]

    Returns:
        list of float: the new offset position.

    Example:
        .. code-block:: python

            self.root = self.addRoot()
            vTemp = tra.getOffsetPosition( self.root, [0,-3,0.1])
            self.knee = self.addLoc("knee", self.root, vTemp)

    """
    offsetVec = dt.Vector(offset[0],offset[1],offset[2])
    return offsetVec + node.getTranslation(space="world")

def getPositionFromMatrix(in_m):
    """
    Get the position values from matrix

    Args:
        in_m (matrix): The input Matrix.

    Returns:
        list of float: The position values for xyz.
    """
    pos = in_m[3][:3]

    return pos

def setMatrixPosition(in_m, pos):
    """
    Set the position for a given matrix

    Args:
        in_m (matrix): The input Matrix.
        pos (list of float): The position values for xyz

    Returns:
        matrix: The matrix with the new position

    >>> tnpo = tra.setMatrixPosition(tOld, tra.getPositionFromMatrix(t))

    >>> t = tra.setMatrixPosition(t, self.guide.apos[-1])
    """
    m = dt.Matrix()
    m[0] = in_m[0]
    m[1] = in_m[1]
    m[2] = in_m[2]
    m[3] = [pos[0], pos[1], pos[2], 1.0]

    return m

def setMatrixRotation(m, rot):
    """
    Set the rotation for a given matrix

    Args:
        in_m (matrix): The input Matrix.
        rot (list of float): The rotation values for xyz

    Returns:
        matrix: The matrix with the new rotation
    """
    X = rot[0]
    Y = rot[1]
    Z = rot[2]

    m[0] = [X[0], X[1], X[2], 0.0]
    m[1] = [Y[0], Y[1], Y[2], 0.0]
    m[2] = [Z[0], Z[1], Z[2], 0.0]

    return m

def setMatrixScale(m, scl=[1,1,1]):
    """
    Set the scale for a given matrix

    Args:
        in_m (matrix): The input Matrix.
        scl (list of float): The scale values for xyz

    Returns:
        matrix: The matrix with the new scale
    """

    tm = dt.TransformationMatrix(m)
    tm.setScale(scl, space="world")

    m = dt.Matrix(tm)

    return m


def getFilteredTransform(m, translation=True, rotation=True, scaling=True):
    """
    Retrieve a transformation filtered.

    Args:
        m (matrix): the reference matrix
        translation (bool): If true the return matrix will match the translation.
        rotation (bool): If true the return matrix will match the rotation.
        scaling (bool): If true the return matrix will match the scaling.

    Returns:
        matrix : The filtered matrix

    """

    t = dt.Vector(m[3][0],m[3][1],m[3][2])
    x = dt.Vector(m[0][0],m[0][1],m[0][2])
    y = dt.Vector(m[1][0],m[1][1],m[1][2])
    z = dt.Vector(m[2][0],m[2][1],m[2][2])

    out = dt.Matrix()

    if translation:
        out = setMatrixPosition(out, t)

    if rotation and scaling:
        out = setMatrixRotation(out, [x,y,z])
    elif rotation and not scaling:
        out = setMatrixRotation(out, [x.normal(), y.normal(), z.normal()])
    elif not rotation and scaling:
        out = setMatrixRotation(out, [dt.Vector(1,0,0) * x.length(), dt.Vector(0,1,0) * y.length(), dt.Vector(0,0,1) * z.length()])

    return out

##########################################################
# ROTATION
##########################################################

def getRotationFromAxis(in_a, in_b, axis="xy", negate=False):
    """
    Get the matrix rotation from a given axis.

    Args:
        in_a (vector): Axis A
        in_b (vector): Axis B
        axis (str): The axis to use for the orientation. Default: "xy"
        negate (bool): negates the axis orientation.

    Returns:
        matrix: The newly created matrix.

    Example:
        .. code-block:: python

            x = dt.Vector(0,-1,0)
            x = x * tra.getTransform(self.eff_loc)
            z = dt.Vector(self.normal.x,self.normal.y,self.normal.z)
            z = z * tra.getTransform(self.eff_loc)
            m = tra.getRotationFromAxis(x, z, "xz", self.negate)
    """

    a = dt.Vector(in_a.x, in_a.y, in_a.z)
    b = dt.Vector(in_b.x, in_b.y, in_b.z)
    c = dt.Vector()

    if negate:
        a *= -1

    a.normalize()
    c = a ^ b
    c.normalize()
    b = c ^ a
    b.normalize()

    if axis == "xy":
      x = a
      y = b
      z = c
    elif axis == "xz":
      x = a
      z = b
      y = -c
    elif axis == "yx":
      y = a
      x = b
      z = -c
    elif axis == "yz":
      y = a
      z = b
      x = c
    elif axis == "zx":
      z = a
      x = b
      y = c
    elif axis == "zy":
      z = a
      y = b
      x = -c

    m = dt.Matrix()
    setMatrixRotation(m, [x,y,z])

    return m

def getSymmetricalTransform(t, axis="yz", fNegScale=False):
    """
    Get the symmetrical tranformation matrix from a define 2 axis mirror plane. exp:"yz".

    Args:
        t (matrix): The transformation matrix to mirror.
        axis (str): The mirror plane.
        fNegScale(bool):  This function is not yet implemented.

    Returns:
        matrix: The symmetrical tranformation matrix.
    """

    if axis == "yz":
        mirror =   dt.TransformationMatrix(-1,0,0,0,
                                            0,1,0,0,
                                            0,0,1,0,
                                            0,0,0,1)

    if axis == "xy":
        mirror =   dt.TransformationMatrix(1,0,0,0,
                                            0,1,0,0,
                                            0,0,-1,0,
                                            0,0,0,1)
    if axis == "zx":
        mirror =   dt.TransformationMatrix(1,0,0,0,
                                            0,-1,0,0,
                                            0,0,1,0,
                                            0,0,0,1)
    t *= mirror

    #TODO: getSymmetricalTransform: add freeze negative scaling procedure.

    return t

def resetTransform(node, t=True, r=True, s=True):
    """
    Reset the scale, rotation and translation for a given dagNode.

    Args:
        node(dagNode): The object to reset the transforms.
        t (bool): If true translation will be reseted.
        r (bool): If true rotation will be reseted.
        s (bool): If true scale will be reseted.

    Returns:
        None

    """

    trsDic = {"tx":0, "ty":0, "tz":0, "rx":0, "ry":0, "rz":0, "sx":1, "sy":1, "sz":1}
    tAxis = ["tx", "ty", "tz"]
    rAxis = ["rx", "ry", "rz"]
    sAxis = ["sx", "sy", "sz"]
    axis = []

    if t: axis =  axis + tAxis
    if r: axis =  axis + rAxis
    if s: axis =  axis + sAxis

    for a in axis:
        try: node.attr(a).set(trsDic[a])
        except: pass




def matchWorldTransform(source, target):
    """
    Match 2 dagNode transformations in world space.

    Args:
        source (dagNode): The source dagNode
        target (dagNode): The target dagNode

    Returns:
        None
    """

    sWM = source.getMatrix(worldSpace=True)
    target.setMatrix(sWM, worldSpace=True)

def quaternionDotProd(q1, q2):
    """
    Get the dot product of 2 quaternion.

    Args:
        q1 (quaternion): Input quaternion 1.
        q2 (quaternion): Input quaternion 2.

    Returns:
        quaternion: The dot proct quaternion.
    """

    dot = q1.x * q2.x + q1.y * q2.y + q1.z * q2.z + q1.w * q2.w
    return dot

def quaternionSlerp(q1, q2, blend):
    """
    Get an interpolate quaternion based in slerp function.

    Args:
        q1 (quaternion): Input quaternion 1.
        q2 (quaternion): Input quaternion 2.
        blend (float): Blending value.

    Returns:
        quaternion: The interpolated quaternion.

    Example:
        .. code-block:: python

            q = quaternionSlerp(dt.Quaternion(t1.getRotationQuaternion()),
                    dt.Quaternion(t2.getRotationQuaternion()), blend)
    """
    dot = quaternionDotProd(q1, q2)
    if dot < 0.0:
        dot = quaternionDotProd(q1, q2.negateIt())

    arcos = math.acos(round(dot, 10))
    sin = math.sin(arcos)

    if sin > 0.001:
        w1 = math.sin((1.0 - blend) * arcos) / sin
        w2 = math.sin(blend * arcos) / sin
    else:
        w1 = 1.0 - blend
        w2 = blend

    result = dt.Quaternion(q1).scaleIt(w1) + dt.Quaternion(q2).scaleIt(w2)

    return result


def convert2TransformMatrix(tm):
    """
    Convert a transformation Matrix or a matrix to a transformation matrix in world space.

    Args:
        tm (matrix): The input matrix.

    Returns:
        matrix: The transformation matrix in worldSpace
    """
    if isinstance(tm, nt.Transform):
        tm = dt.TransformationMatrix(tm.getMatrix(worldSpace=True))
    if isinstance(tm, dt.Matrix):
        tm = dt.TransformationMatrix(tm)

    return tm


def getInterpolateTransformMatrix(t1, t2, blend=.5 ):
    """
    Interpolate 2 matrix.

    Args:
        t1 (matrix): Input matrix 1.
        t2 (matrix): Input matrix 2.
        blend (float): The blending value. Default 0.5

    Returns:
        matrix: The newly interpolated transformation matrix.

    >>> t = tra.getInterpolateTransformMatrix(self.fk_ctl[0], self.tws1A_npo, .3333)
    """

    #check if the input transforms are transformMatrix
    t1 = convert2TransformMatrix(t1)
    t2 = convert2TransformMatrix(t2)

    if (blend == 1.0):
        return t2
    elif (blend == 0.0):
        return t1

    # translate
    pos = vec.linearlyInterpolate(t1.getTranslation(space="world"),
            t2.getTranslation(space="world"), blend)

    # scale
    scaleA = dt.Vector(*t1.getScale(space="world"))
    scaleB = dt.Vector(*t2.getScale(space="world"))


    vs = vec.linearlyInterpolate(scaleA, scaleB, blend)

    # rotate
    q = quaternionSlerp(dt.Quaternion(t1.getRotationQuaternion()),
        dt.Quaternion(t2.getRotationQuaternion()), blend)

    # out
    result = dt.TransformationMatrix()

    result.setTranslation(pos, space="world")
    result.setRotationQuaternion(q.x, q.y, q.z, q.w)
    result.setScale([vs.x, vs.y, vs.z], space="world")

    return result
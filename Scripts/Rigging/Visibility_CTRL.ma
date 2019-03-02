//Maya ASCII 2009 scene
//Name: Visibility_CTRL.ma
//Last modified: Fri, Mar 26, 2010 11:16:57 AM
//Codeset: 1252
requires maya "2009";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya Unlimited 2009";
fileInfo "version" "2009 Service Pack 1a";
fileInfo "cutIdentifier" "200904080023-749524";
fileInfo "osv" "Microsoft Windows XP x64 Service Pack 2 (Build 3790)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 12.789399613869874 13.17687777035103 24.998243467041149 ;
	setAttr ".r" -type "double3" -24.938352729602457 23.79999999999999 -6.6047216146499551e-014 ;
	setAttr ".rp" -type "double3" -6.6613381477509392e-016 2.2204460492503131e-016 0 ;
	setAttr ".rpt" -type "double3" 1.8866907266987703e-017 -2.0702999857483352e-017 
		1.8315341732233302e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999979;
	setAttr ".coi" 30.945149792125154;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -1.0226907693110405 0.52024986892581282 0.22340666880808158 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Visibility_Ctrl_Grp";
createNode transform -n "Visibility_Ctrl" -p "Visibility_Ctrl_Grp";
	addAttr -ci true -sn "CTRLVisibilityAttr" -ln "CTRLVisibilityAttr" -nn "CTRL Visibility  Attr" 
		-min 0 -max 0 -en "***********" -at "enum";
	addAttr -ci true -sn "FacialVis" -ln "FacialVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HeadVis" -ln "HeadVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "EyeVis" -ln "EyeVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "SpineVis" -ln "SpineVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HandsVis" -ln "HandsVis" -min 0 -max 0 -en "**********" -at "enum";
	addAttr -ci true -sn "R_Hand" -ln "R_Hand" -nn "R Hand" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Hand" -ln "L_Hand" -nn "L Hand" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "FingersVis" -ln "FingersVis" -min 0 -max 0 -en "*************" 
		-at "enum";
	addAttr -ci true -sn "LH_Fingers" -ln "LH_Fingers" -nn "LH Fingers" -min 0 -max 
		1 -at "bool";
	addAttr -ci true -sn "RH_Fingers" -ln "RH_Fingers" -nn "RH Fingers" -min 0 -max 
		1 -at "bool";
	addAttr -ci true -sn "LegsVis" -ln "LegsVis" -min 0 -max 0 -en "*********" -at "enum";
	addAttr -ci true -sn "L_Leg" -ln "L_Leg" -nn "L Leg" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Leg" -ln "R_Leg" -nn "R Leg" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "MeshDisp" -ln "MeshDisp" -min 0 -max 0 -en "*********" -at "enum";
	addAttr -ci true -sn "MeshSelection" -ln "MeshSelection" -min 0 -max 2 -en "Normal:Template:Reference" 
		-at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.1102230246251565e-016 0 0 ;
	setAttr ".sp" -type "double3" -1.1102230246251565e-016 0 0 ;
	setAttr -l on -cb on ".CTRLVisibilityAttr";
	setAttr -cb on ".FacialVis" yes;
	setAttr -cb on ".HeadVis" yes;
	setAttr -cb on ".EyeVis" yes;
	setAttr -cb on ".SpineVis" yes;
	setAttr -l on -cb on ".HandsVis";
	setAttr -cb on ".R_Hand" yes;
	setAttr -cb on ".L_Hand" yes;
	setAttr -l on -cb on ".FingersVis";
	setAttr -cb on ".LH_Fingers" yes;
	setAttr -cb on ".RH_Fingers" yes;
	setAttr -l on -cb on ".LegsVis";
	setAttr -cb on ".L_Leg" yes;
	setAttr -cb on ".R_Leg" yes;
	setAttr -l on -cb on ".MeshDisp";
	setAttr -cb on ".MeshSelection";
createNode nurbsCurve -n "Visibility_CtrlShape" -p "Visibility_Ctrl";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		2 40 1 no 3
		43 0 0 0.89999999999999991 0.89999999999999991 1 1 2 3 3 4 5 5 6 6 7 8 9 9
		 10 11 11 11.223437857633325 11.223437857633325 12.223437857633325 13.223437857633325
		 13.223437857633325 14.223437857633325 15.223437857633325 16.223437857633325 16.223437857633325
		 17.223437857633325 18.223437857633325 19.223437857633325 19.223437857633325 20.223437857633325
		 20.223437857633325 21.223437857633325 21.223437857633325 22.223437857633325 23.223437857633325
		 23.223437857633325 23.323437857633326 23.323437857633326
		42
		1.625996476207777 3.9113072393313635e-016 -1.7614961825584252
		1.625996476207777 2.5573931949474313e-016 -1.1517475039805094
		1.625996476207777 1.2034791505634972e-016 -0.5419988254025927
		1.5582466230324528 1.2034791505634972e-016 -0.5419988254025927
		1.490496769857129 1.2034791505634972e-016 -0.5419988254025927
		1.3825208613387816 2.2236175676343807e-016 -1.0014283249012685
		0.79606258395392082 3.3095676640496167e-016 -1.4904967698571296
		0.42555405601276775 3.3095676640496167e-016 -1.4904967698571296
		0.11432962176494144 3.3095676640496167e-016 -1.4904967698571296
		-0.40438190383407502 2.5244873552752556e-016 -1.136928031251917
		-0.52294388844176898 1.8945408069979245e-016 -0.85322532724340516
		-0.67749853175324048 1.0812535252279822e-016 -0.48695329733097759
		-0.67749853175324048 8.9322081152679966e-018 -0.04022708913951667
		-0.67749853175324048 -8.8380471425890031e-017 0.39803025818046711
		-0.45731021668782112 -2.4868734669691336e-016 1.1199882419159763
		0.01482050652508482 -3.3095676640496152e-016 1.490496769857129
		0.38744624968410735 -3.3095676640496152e-016 1.490496769857129
		0.69655346871406421 -3.3095676640496152e-016 1.490496769857129
		1.2067961334416033 -2.6890234401041449e-016 1.2110284962843556
		1.490496769857129 -1.92744435118076e-016 0.86804376617550383
		1.4904967698571294 -2.263572855066113e-016 1.0194225866601716
		1.4904967698571294 -2.5997013589514654e-016 1.1708014071448392
		1.2089133486594728 -3.2907630153858932e-016 1.4820279089856518
		0.59916363628506319 -3.9113072393313635e-016 1.7614961825584252
		0.19266451723311917 -3.9113072393313635e-016 1.7614961825584252
		-0.34298266251586562 -3.9113072393313635e-016 1.7614961825584252
		-1.1750358375805781 -2.9522839304175748e-016 1.3295904808920493
		-1.6259964762077772 -1.1517663667382607e-016 0.51870945800603008
		-1.6259964762077772 -1.3632911183330658e-017 0.06139717372522302
		-1.6259964762077772 9.3081633591820547e-017 -0.41920241035916006
		-1.1178710266981073 2.8535641159117117e-016 -1.2851310289097804
		-0.2561789061762112 3.9113072393313635e-016 -1.7614961825584252
		0.22865717593689672 3.9113072393313635e-016 -1.7614961825584252
		0.58646034497784694 3.9113072393313635e-016 -1.7614961825584252
		0.98237338794044549 3.5305222858483504e-016 -1.5900058850969863
		1.2131477790952112 3.3095676640496167e-016 -1.4904967698571296
		1.2745449528204342 3.3095676640496167e-016 -1.4904967698571296
		1.3549970635064814 3.3095676640496167e-016 -1.4904967698571296
		1.4735611157071613 3.5963385561713765e-016 -1.6196468981471559
		1.490496769857129 3.9113072393313635e-016 -1.7614961825584252
		1.5582466230324528 3.9113072393313635e-016 -1.7614961825584252
		1.625996476207777 3.9113072393313635e-016 -1.7614961825584252
		;
createNode lightLinker -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :lightList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".fs" 1;
	setAttr ".ef" 10;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
connectAttr ":defaultLightSet.msg" "lightLinker1.lnk[0].llnk";
connectAttr ":initialShadingGroup.msg" "lightLinker1.lnk[0].olnk";
connectAttr ":defaultLightSet.msg" "lightLinker1.lnk[1].llnk";
connectAttr ":initialParticleSE.msg" "lightLinker1.lnk[1].olnk";
connectAttr ":defaultLightSet.msg" "lightLinker1.slnk[0].sllk";
connectAttr ":initialShadingGroup.msg" "lightLinker1.slnk[0].solk";
connectAttr ":defaultLightSet.msg" "lightLinker1.slnk[1].sllk";
connectAttr ":initialParticleSE.msg" "lightLinker1.slnk[1].solk";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "lightLinker1.msg" ":lightList1.ln" -na;
// End of Visibility_CTRL.ma

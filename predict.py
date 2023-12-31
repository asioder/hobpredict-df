import deepchem
import sys
import pickle
import numpy as np


mordred_columns_to_delete = [5,6,8,9,11,20,24,29,32,33,143,147,148,188
,189,190,191,192,193,197,198,199,200,201,202,207,208,209
,210,215,216,217,218,219,220,221,222,223,234,235,236,237
,238,239,240,241,341,342,343,344,345,346,347,348,349,359
,360,361,362,363,364,365,366,367,369,371,404,405,406,407
,408,409,410,411,412,413,414,415,416,417,418,419,420,421
,422,423,424,425,426,427,428,429,430,431,432,433,434,435
,436,437,438,439,440,441,442,443,444,445,446,447,448,449
,450,451,452,453,454,455,456,457,458,459,460,461,462,463
,464,465,466,467,468,469,470,471,472,473,474,475,476,477
,478,479,480,481,482,483,484,485,486,487,488,489,490,491
,492,493,494,495,496,497,498,499,500,501,502,503,504,505
,506,507,508,509,510,511,512,513,514,515,516,517,518,519
,520,521,522,523,524,525,526,527,528,529,530,531,532,533
,534,535,536,537,538,539,540,541,542,543,544,545,546,547
,548,549,550,551,552,553,554,555,556,557,558,559,560,561
,562,563,564,565,566,567,568,569,570,571,572,573,574,577
,578,579,580,581,582,583,584,585,586,587,588,589,590,591
,592,593,594,595,596,597,598,599,600,601,602,603,604,605
,606,607,609,610,611,612,613,614,615,617,618,619,620,621
,622,623,625,626,627,628,629,630,631,632,633,634,635,636
,637,638,639,640,641,642,645,646,648,650,652,655,656,657
,658,659,660,662,664,674,687,700,713,726,739,752,765,775
,780,781,782,783,791,792,793,794,795,796,797,798,799,800
,801,802,804,806,808,809,810,825,826,827,828,829,830,831
,832,841,842,843,844,845,846,847,848,857,858,859,860,861
,862,863,864,865,866,867,868,869,870,871,872,873,874,875
,876,877,878,886,891,892,893,894,895,896,898,900,904,905
,910,912,913,915,916,917,921,923,927,929,930,931,932,933
,934,935,936,937,938,939,940,941,942,943,945,946,947,948
,949,950,951,952,953,954,955,956,957,958,959,960,961,962
,963,964,965,966,967,968,969,970,971,972,973,974,975,983
,989,991,996,1000,1002,1008,1009,1010,1011,1012,1013,1014,1016,1018
,1020,1021,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035
,1036,1037,1038,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050
,1051,1052,1053,1054,1062,1066,1068,1070,1075,1079,1081,1087,1088,1089
,1090,1091,1092,1093,1095,1097,1098,1099,1100,1103,1104,1105,1106,1107
,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121
,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1141,1145
,1147,1149,1154,1158,1160,1166,1167,1168,1169,1170,1171,1172,1174,1176
,1177,1178,1179,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192
,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,1203,1204,1205,1206
,1209,1210,1211,1212,1214,1216,1218,1220,1222,1224,1226,1228,1230,1232
,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246
,1247,1249,1250,1251,1252,1254,1257,1258,1269,1270,1271,1272,1273,1274
,1275,1276,1277,1278,1279,1280,1284,1285,1286,1302,1303,1327,1337,1368
,1372,1373,1374,1377,1379,1381,1383,1385,1387,1389,1400,1401,1414,1415
,1418,1419,1420,1421,1422,1423,1424,1426,1427,1430,1431,1432,1433,1434
,1435,1436,1438,1439,1442,1443,1444,1445,1446,1447,1448,1450,1451,1454
,1455,1456,1457,1458,1459,1460,1462,1463,1466,1467,1468,1469,1470,1471
,1472,1474,1475,1478,1479,1480,1481,1482,1483,1484,1486,1487,1488,1489
,1490,1491,1492,1493,1494,1495,1497,1498,1499,1500,1501,1502,1503,1504
,1505,1506,1507,1508,1509,1510,1511,1512,1513,1514,1515,1516,1517,1518
,1519,1520,1521,1522,1523,1524,1525,1526,1527,1528,1530,1531,1532,1533
,1534,1535,1536,1537,1538,1539,1541,1542,1543,1544,1545,1546,1547,1548
,1549,1550,1552,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573
,1574,1575,1576,1577,1580,1581,1585,1595,1596,1597]

rdkit_columns_to_delete = [2,4,9,10,11,12,13,14,15,16,18,19,20,21,22,24,25,41
,68,81,104,124,127,128,130,136,137,142,143,144,145,146,147,148,152,155
,156,157,159,161,162,163,166,167,169,170,171,172,173,174,176,177,178,180
,181,182,183,184,185,186,187,191,192,194,195,196,197,198,199,200,201,202
,203,204,205,206,208]

def featurize(smile_path, feature_name=''):
    feature_classes = {
        'maccskeys': deepchem.feat.MACCSKeysFingerprint,
        'circular': deepchem.feat.CircularFingerprint,
        'mol2vec': deepchem.feat.Mol2VecFingerprint,
        'mordred': lambda: deepchem.feat.MordredDescriptors(ignore_3D=True),
        'rdkit': deepchem.feat.RDKitDescriptors,
        'pubchem': deepchem.feat.PubChemFingerprint
    }

    # Select the appropriate feature class, and use the default value if feature_name is not specified or in the dictionary
    feature_class = feature_classes.get(feature_name, lambda: deepchem.feat.MordredDescriptors(ignore_3D=True))

    # Create an instance of the feature
    feature = feature_class()
    with open(smile_path,'r') as smiles_data:
        smile_feature = feature.featurize(smiles_data)

    return smile_feature

def load_dfmodel(cutoff):
    if cutoff == '20':
        file_path = "model/{}_model_20.pkl".format(feature_name)
        df_model = pickle.load(open(file_path, 'rb'))
    if cutoff == '50':
        file_path = "model/{}_model_50.pkl".format(feature_name)
        df_model = pickle.load(open(file_path, 'rb'))
    return df_model

# Check the number of parameters entered
num_args = len(sys.argv) - 1
# When there are two parameters
if num_args == 2:
    smile_path = sys.argv[1]
    cutoff = sys.argv[2]
    feature_name = 'mordred'  # feature_name 没有提供
# When there are three parameters
elif num_args == 3:
    smile_path = sys.argv[1]
    feature_name = sys.argv[2]
    cutoff = sys.argv[3]
else:
    # If the number of parameters is incorrect, an error message is printed
    print("Usage: script_name smile_path [feature_name] cutoff")
    sys.exit(1)

# Open the original file
with open(smile_path, 'r') as file:
    lines = file.readlines()

# Remove blank lines
non_empty_lines = [line for line in lines if line.strip()]

# Write the processed content back to the file
with open(smile_path, 'w') as file:
    file.writelines(non_empty_lines)

smile_feature = featurize(smile_path,feature_name)
print(smile_feature.shape)
print(feature_name)

if feature_name == 'maccskeys' or feature_name =='circular' or feature_name =='mol2vec' or feature_name =='pubchem':
    # Feature data preprocessing
    smile_feature[np.isnan(smile_feature)] = 0

elif feature_name == '' or feature_name =='mordred':
    # Feature data preprocessing
    smile_feature[np.isnan(smile_feature)] = 0
    # Delete these columns
    smile_feature = np.delete(smile_feature, mordred_columns_to_delete, axis=1)
elif feature_name =='rdkit':
    # Feature data preprocessing
    smile_feature[np.isnan(smile_feature)] = 0
    # Delete these columns
    smile_feature = np.delete(smile_feature, rdkit_columns_to_delete, axis=1)


print(smile_feature.shape)
df_model = load_dfmodel(cutoff)
y_pred_tests = df_model.predict(smile_feature)
probabilities = df_model.predict_proba(smile_feature)
for y_pred_test in y_pred_tests:
    print("high" if y_pred_test == 1 else "low")
print(probabilities)

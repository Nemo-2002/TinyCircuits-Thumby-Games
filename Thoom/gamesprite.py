
import thumby
# BITMAP: width: 72, height: 40
BG = bytearray([162,69,170,5,162,85,162,245,186,245,170,221,186,125,174,223,171,127,190,255,187,127,255,255,187,255,255,255,187,127,187,255,171,255,255,255,187,127,175,255,171,87,171,159,171,87,171,223,139,87,171,31,171,23,171,85,11,69,171,21,171,7,170,65,130,85,162,213,162,81,170,193,
           186,255,250,255,186,117,186,221,168,253,168,249,170,127,174,255,170,119,170,223,170,103,170,253,170,117,234,245,170,241,232,245,170,245,234,249,170,245,232,253,184,245,234,253,170,245,234,253,186,244,250,253,186,247,234,253,170,247,234,253,170,247,234,253,186,255,250,253,186,253,250,253,
           253,235,253,183,253,235,252,247,252,235,252,183,252,235,252,247,253,235,252,183,252,235,252,247,252,235,252,183,252,235,252,247,253,235,253,183,253,235,253,247,253,235,253,183,253,235,252,247,252,235,252,183,252,235,252,247,252,235,252,183,252,235,252,247,252,235,252,183,253,235,253,247,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])

# BITMAP: width: 24, height: 12

NormWall = bytearray([0,0,228,238,238,238,238,238,238,238,228,0,0,228,238,238,238,238,238,238,238,228,0,0,
            0,0,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,0,0])
        # BITMAP: width: 24, height: 12
DoorWall = bytearray([0,254,254,254,0,0,254,2,2,2,2,2,2,2,6,198,6,254,0,0,254,254,254,0,
            0,3,3,3,0,0,15,8,8,8,8,8,8,8,8,8,8,15,0,0,3,3,3,0])
            # BITMAP: width: 24, height: 12
IconWall = bytearray([0,254,248,248,250,242,2,6,230,52,112,248,248,112,52,230,6,2,242,250,248,248,254,0,
           0,3,3,3,3,3,3,0,0,3,7,3,3,7,3,0,0,3,3,3,3,3,3,0])
           # BITMAP: width: 24, height: 12
IconWall2 = bytearray([0,254,248,248,250,242,2,6,246,148,184,248,248,184,148,246,6,2,242,250,248,248,254,0,
           0,3,3,3,3,3,2,0,0,5,11,9,9,11,5,0,0,2,3,3,3,3,3,0])
           # BITMAP: width: 24, height: 12
IconWallB = bytearray([0,15,8,8,26,242,2,2,250,212,228,252,252,228,212,250,2,2,242,26,8,8,15,0,
           0,0,0,0,0,3,14,0,0,5,8,8,8,8,5,0,0,14,3,0,0,0,0,0])
           # BITMAP: width: 24, height: 12
IconWallD = bytearray([15,15,59,33,41,233,13,5,229,245,113,240,248,56,116,230,6,2,242,26,8,8,15,15,
           0,0,0,0,0,7,12,0,3,6,2,7,7,7,7,3,0,12,7,0,0,0,0,0])
           # BITMAP: width: 24, height: 12
DangerWall = bytearray([0,0,254,254,254,0,0,254,254,254,254,0,0,254,254,254,254,0,0,254,254,254,0,0,
           6,6,2,0,0,4,6,6,2,0,0,4,6,6,2,0,0,4,6,6,2,0,0,4])
           # BITMAP: width: 24, height: 12
HexoWall = bytearray([112,112,112,112,36,142,142,142,142,142,36,112,112,112,112,112,36,142,142,142,142,142,36,112,
           0,0,0,0,1,3,3,3,3,3,1,0,0,0,0,0,1,3,3,3,3,3,1,0])
           # BITMAP: width: 24, height: 12
BrickWall = bytearray([224,224,238,14,14,238,238,238,224,224,238,14,14,238,238,238,224,224,238,14,14,238,238,238,
           0,0,14,14,14,14,14,14,0,0,14,14,14,14,14,14,0,0,14,14,14,14,14,14])
           # BITMAP: width: 24, height: 12
SpecialWall = bytearray([0,0,158,158,158,0,0,254,0,254,254,194,226,254,254,0,254,0,0,158,158,158,0,0,
           0,0,3,3,3,0,0,15,0,7,3,1,1,3,7,0,15,0,0,3,3,3,0,0])
            
# BITMAP: width: 72, height: 40
Title = bytearray([255,1,1,129,193,1,1,1,1,1,193,129,1,1,255,1,1,1,1,1,63,63,63,1,1,1,1,1,253,3,1,1,1,1,193,193,193,1,1,1,1,3,255,3,1,1,1,1,193,193,193,1,1,1,1,3,253,1,1,1,1,1,15,63,7,1,1,1,1,1,253,255,
           255,254,255,255,255,0,192,224,240,0,255,255,255,254,255,0,240,224,192,0,248,248,248,0,248,252,254,0,255,0,254,252,248,0,255,255,255,0,0,0,0,0,255,0,0,0,0,0,255,255,255,0,248,252,254,0,255,0,254,252,248,0,224,192,128,0,0,0,0,0,255,255,
           255,255,255,255,255,0,255,255,255,0,255,255,255,255,255,0,63,31,143,192,239,255,255,0,63,31,143,192,239,240,231,207,159,62,125,251,247,224,127,62,28,128,255,128,28,62,127,224,247,251,125,62,159,207,231,240,239,192,143,31,63,0,248,195,248,0,255,254,252,0,255,255,
           255,255,255,255,239,192,227,241,248,252,254,255,255,255,254,252,254,255,255,255,255,255,254,252,254,255,255,255,255,255,255,255,127,63,62,60,57,56,124,254,255,255,255,255,255,254,252,248,249,252,254,255,255,255,255,255,255,255,255,255,254,252,255,255,251,240,231,207,159,128,191,255,
           255,226,226,250,248,248,255,226,226,250,224,228,255,241,224,234,234,234,255,232,232,234,226,226,255,232,232,234,226,226,255,224,192,159,159,149,159,138,192,224,255,232,232,234,226,226,255,254,254,224,224,254,238,231,243,249,250,224,225,255,226,226,250,224,228,255,254,254,224,224,254,254])

# BITMAP: width: 15, height: 7
shotgun =  bytearray([112,12,2,1,1,1,2,124,2,1,1,1,2,12,112])
# BITMAP: width: 15, height: 7
shotgunM = bytearray([112,124,126,127,127,127,126,124,126,127,127,127,126,124,112])

          
# BITMAP: width: 47, height: 15
shotgun_idle = bytearray([124,70,195,129,129,3,7,5,9,9,17,19,50,38,36,100,76,200,136,152,16,48,32,32,96,64,64,192,128,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,1,15,24,22,54,44,108,88,88,48,48,96,96,96,64,65,1,1,3,2,2,4,4,8,8,16,17,17,49,3,2,18,22,52,36,4,12,40,104,88,80,48,96])
# BITMAP: width: 47, height: 15
shotgun_idleM = bytearray([124,126,255,255,255,255,255,255,255,255,255,255,254,254,252,252,252,248,248,248,240,240,224,224,224,192,192,192,128,128,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,1,15,31,31,63,63,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,126,126,126,124,124,124,124,120,120,120,112,112,96])
       
           # BITMAP: width: 18, height: 17
shotgun_blast = bytearray([0,0,0,0,0,0,0,0,32,64,0,0,0,0,236,0,0,0,
           0,0,0,32,32,36,36,44,36,184,120,126,250,255,255,244,248,112,
           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
           # BITMAP: width: 18, height: 17
shotgun_blastM = bytearray([0,0,0,0,0,0,0,48,96,224,192,128,192,240,255,192,0,0,
           32,32,32,50,50,118,126,254,254,254,255,255,255,255,255,255,254,124,
           0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0])
           
       # BITMAP: width: 25, height: 19
shotgun_reload = bytearray([0,0,0,0,0,0,128,224,112,144,224,240,240,120,28,14,134,206,156,120,112,0,0,0,0,
            0,0,0,128,240,254,255,255,255,255,255,127,118,48,56,57,27,25,29,12,32,126,124,48,0,
            0,6,7,7,6,6,6,6,6,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0])    
            # BITMAP: width: 25, height: 19
shotgun_reloadM = bytearray([0,0,0,192,224,240,248,248,248,248,248,248,252,254,255,255,255,255,255,252,252,248,0,0,0,
            0,128,248,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,127,255,255,254,252,120,
            6,7,7,7,7,7,7,7,7,7,7,7,7,1,0,0,0,0,0,0,0,0,0,0,0])
           
# BITMAP: width: 22, height: 32
imp32 = [thumby.Sprite(22, 32,bytearray([0,0,0,0,0,0,0,0,224,44,60,44,228,0,0,0,0,0,0,0,0,0,
           0,0,96,56,30,15,15,14,253,186,202,186,189,254,15,15,15,28,56,192,0,0,
           0,0,4,0,0,0,0,60,191,249,7,7,1,191,62,0,0,0,2,1,0,0,
           0,0,0,0,0,0,0,0,0,3,0,0,0,15,0,0,0,0,0,0,0,0])),
           thumby.Sprite(22, 32,bytearray([0,0,128,128,0,128,128,248,252,254,254,254,254,252,128,128,128,128,64,0,0,0,
           32,224,252,254,63,31,31,255,255,255,255,255,255,255,255,31,31,63,252,248,192,32,
           0,15,15,12,0,0,60,255,255,255,255,15,255,255,255,126,0,14,15,3,1,0,
           0,0,0,0,0,0,0,32,55,31,63,32,31,31,15,0,0,0,0,0,0,0]))]
          
# BITMAP: width: 16, height: 24
imp24 = [thumby.Sprite(16, 24,bytearray([0,0,128,192,224,128,124,76,124,128,224,192,128,0,0,0,
           0,3,0,0,0,243,123,59,127,243,0,0,0,3,0,0,
           0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])),
           thumby.Sprite(16, 24,bytearray([0,144,224,224,240,252,254,254,254,252,240,224,224,144,0,0,
           127,111,3,1,243,255,255,127,255,255,243,1,99,127,31,0,
           0,0,0,0,67,127,127,64,3,63,31,0,0,0,0,0]))]
# BITMAP: width: 14, height: 18
imp18 = [thumby.Sprite(14, 18,bytearray([127,23,143,183,183,96,238,224,119,183,175,23,127,255,
           248,240,255,255,225,12,51,251,12,129,243,240,252,255,
           3,3,3,3,3,0,0,3,2,3,3,3,3,3])),
           thumby.Sprite(14, 18,bytearray([128,232,112,120,120,255,255,255,248,120,112,232,128,0,
            7,15,0,0,30,255,207,7,255,126,12,15,3,0,
            0,0,0,0,0,3,3,0,1,0,0,0,0,0]))]
           
           # BITMAP: width: 10, height: 14
imp14 = [thumby.Sprite(10, 14,bytearray([0,32,16,8,176,246,176,8,16,0,
           0,0,0,0,3,0,0,0,0,0])),
           thumby.Sprite(10, 14,bytearray([224,240,56,252,255,255,255,252,56,240,
           1,1,0,7,63,1,15,3,0,1]))]
           
# BITMAP: width: 8, height: 10
imp10 = [thumby.Sprite(8, 10,bytearray([207,211,8,206,62,200,147,199,
           3,3,0,1,2,2,3,3])),
           thumby.Sprite(8, 10,bytearray([48,60,255,255,255,255,124,56,
           0,0,3,3,1,1,0,0]))]
# BITMAP: width: 5, height: 6
imp6 = [thumby.Sprite(5, 6,bytearray([51,4,30,36,59])),
            thumby.Sprite(5, 6,bytearray([12,63,63,31,12]))]

# BITMAP: width: 22, height: 32
imp32B = [thumby.Sprite(22, 32,bytearray([0,0,0,0,0,0,0,0,0,128,128,224,192,192,192,192,0,0,0,0,0,0,
           0,0,128,128,192,64,32,32,48,2,241,231,7,131,231,195,67,0,96,224,192,0,
           0,1,3,3,1,0,0,112,252,62,7,7,2,255,255,255,0,0,0,16,63,0,
           0,0,0,0,0,0,0,0,1,0,0,0,0,31,3,0,0,0,0,0,0,0])),
           thumby.Sprite(22, 32,bytearray([0,0,16,48,32,32,112,226,198,255,252,240,248,254,255,248,244,238,230,167,33,0,
           32,226,198,194,232,252,255,119,255,255,255,255,255,255,255,255,239,255,247,243,226,194,
           3,3,15,7,3,17,248,254,255,255,127,31,255,255,255,255,255,0,51,63,127,63,
           0,0,0,0,0,16,56,59,31,25,206,224,127,127,255,199,129,0,0,0,0,0]))]
           
# BITMAP: width: 16, height: 24
imp24B = [thumby.Sprite(16, 24,bytearray([255,115,243,255,55,143,141,195,231,225,192,195,73,13,156,223,
           231,151,219,226,52,208,225,241,65,227,199,2,240,101,125,3,
           255,255,255,255,220,203,199,224,127,0,7,48,255,255,255,255])),
           thumby.Sprite(16, 24,bytearray([0,140,12,0,200,240,242,252,248,254,255,252,246,242,99,32,
           24,120,60,29,207,239,255,255,255,255,255,255,15,158,254,252,
           0,0,0,0,35,55,63,31,128,255,255,207,0,0,0,0]))]
          
# BITMAP: width: 14, height: 18
imp18B = [thumby.Sprite(14, 18,bytearray([127,219,219,51,70,1,19,59,57,176,3,5,206,223,
           253,250,250,124,3,28,230,246,7,63,192,252,249,243,
           3,3,3,3,3,3,1,0,2,0,1,3,3,3])),
           thumby.Sprite(14, 18,bytearray([128,36,36,204,185,254,252,252,254,255,252,250,49,32,
           2,7,7,131,252,255,31,15,255,255,63,3,6,12,
           0,0,0,0,0,0,2,3,1,3,2,0,0,0]))]
           
# BITMAP: width: 10, height: 14
imp14B = [thumby.Sprite(10, 14,bytearray([0,0,0,0,24,156,136,0,0,0,
           0,0,0,0,1,1,3,0,0,0])),
           thumby.Sprite(10, 14,bytearray([200,234,60,253,254,254,255,252,253,196,
           0,0,16,31,7,51,63,15,0,3]))]
           
          # BITMAP: width: 8, height: 10
imp10B = [thumby.Sprite(8, 10,bytearray([199,147,200,48,192,8,211,206,
           3,3,2,2,1,0,3,3])),
           thumby.Sprite(8, 10,bytearray([56,124,255,255,255,255,60,49,
            0,0,1,1,3,3,0,0]))]
            
            
# BITMAP: width: 22, height: 11
imp32D = [thumby.Sprite(22, 11,bytearray([255,255,127,127,15,35,153,205,140,57,59,3,253,253,57,7,63,63,63,63,63,63,
           4,4,4,4,4,6,7,7,7,7,2,0,1,0,1,6,6,6,6,7,5,7])),
           thumby.Sprite(22, 11,bytearray([0,0,128,128,240,252,126,62,127,254,252,252,254,254,254,248,192,192,192,192,192,192,
           3,3,3,3,3,1,0,0,0,0,5,7,7,7,6,1,1,1,1,0,2,0]))]
           
# BITMAP: width: 16, height: 8
imp24D = [thumby.Sprite(16, 8,bytearray([191,159,159,131,237,246,230,97,29,61,195,135,143,143,207,207])),
            thumby.Sprite(16, 8,bytearray([64,96,96,124,30,15,31,158,254,254,60,120,112,112,48,48]))]

# BITMAP: width: 14, height: 7
imp18D = [thumby.Sprite(14, 7,bytearray([95,79,67,77,118,2,29,109,99,79,79,79,111,111])),
            thumby.Sprite(14, 7,bytearray([32,48,60,62,15,127,126,30,28,48,48,48,16,16]))]

# BITMAP: width: 8, height: 4
imp14D = [thumby.Sprite(8, 4,bytearray([7,1,9,0,0,11,11,11])),
            thumby.Sprite(8, 4,bytearray([8,14,6,15,15,4,4,4]))]
            
            # BITMAP: width: 16, height: 16
key16 = [thumby.Sprite(16, 16,bytearray([0,224,248,124,156,94,222,94,222,94,222,28,252,248,224,0,
           0,7,31,56,57,121,113,115,115,115,115,48,63,31,7,0])),
            thumby.Sprite(16,16,bytearray([224,248,252,254,254,255,255,255,255,255,255,254,254,252,248,224,
            7,31,63,127,127,255,255,255,255,255,255,127,127,63,31,7]))]
            
            # BITMAP: width: 12, height: 12
key12 = [thumby.Sprite(12, 12,bytearray([240,28,100,86,118,214,246,214,246,4,252,0,
           1,2,6,6,4,4,4,4,4,4,3,0])),
            thumby.Sprite(12,12,bytearray([248,252,254,255,255,255,255,255,255,254,252,248,
           1,3,7,15,15,15,15,15,15,7,3,1]))]
           # BITMAP: width: 8, height: 8
key8 = [thumby.Sprite(8, 8,bytearray([0,60,102,70,86,70,60,0])),
            thumby.Sprite(8, 8,bytearray([60,126,255,255,255,255,126,60]))]
            
            # BITMAP: width: 24, height: 32
demon32 = [thumby.Sprite(24, 32,bytearray([255,255,31,7,11,59,11,51,51,123,123,251,241,222,229,251,251,103,23,239,239,239,31,255,
           255,3,0,0,98,251,240,15,175,175,207,210,223,195,175,174,206,14,240,6,133,225,16,255,
           255,252,252,252,14,243,192,0,31,144,217,208,208,217,208,143,51,216,124,62,31,193,254,255,
           255,223,207,215,151,120,63,143,192,203,215,207,223,255,247,243,224,224,224,242,247,255,255,255])),
           thumby.Sprite(24, 32,bytearray([0,0,224,248,252,252,252,252,252,252,252,252,254,255,254,252,252,248,248,240,240,240,224,0,
           0,252,255,255,159,7,15,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,239,0,
           0,3,3,3,241,252,255,255,255,127,63,63,63,63,63,127,255,255,255,255,255,63,1,0,
           0,32,48,56,120,255,255,127,63,60,56,48,32,0,8,12,31,31,31,13,8,0,0,0]))]
           
           # BITMAP: width: 18, height: 24
demon24 =  [thumby.Sprite(18, 24,bytearray([63,15,7,179,13,229,233,253,253,61,254,253,233,11,183,55,119,7,
           192,192,200,124,60,0,248,138,156,140,204,138,56,222,192,240,60,0,
           255,159,175,176,127,62,128,174,158,254,238,230,192,193,225,237,252,255])),
           thumby.Sprite(18, 24,bytearray([192,240,248,252,254,254,254,254,254,254,255,254,254,252,248,248,248,248,
           63,63,55,131,195,255,255,255,255,255,255,255,255,255,255,255,255,255,
           0,96,112,127,255,255,127,113,97,1,17,25,63,63,31,19,3,0]))]
           
           # BITMAP: width: 14, height: 18
demon18 =  [thumby.Sprite(14, 18,bytearray([15,115,141,13,33,189,61,29,60,189,35,11,203,3,
           252,252,15,240,239,9,233,233,233,7,25,28,223,192,
           3,0,1,1,1,0,3,3,3,3,3,3,3,3])),
            thumby.Sprite(14, 18,bytearray([240,252,126,254,254,254,254,254,255,254,252,252,252,252,
           3,3,240,255,255,255,31,31,31,255,255,255,63,63,
           0,3,3,3,3,3,0,0,0,0,0,0,0,0]))]  
           
           # BITMAP: width: 11, height: 14
demon14 = [thumby.Sprite(11, 14,bytearray([7,27,237,1,93,125,124,221,1,253,3,
           63,15,17,30,1,61,61,32,35,59,56])),
          thumby.Sprite(11, 14,bytearray([248,252,30,254,254,254,255,254,254,254,252,
           0,48,62,63,63,3,3,31,31,7,7]))]
           
           # BITMAP: width: 8, height: 10
demon10 = [thumby.Sprite(8, 10,bytearray([193,5,249,189,60,9,115,135,
            3,0,0,3,2,2,3,3])),
            thumby.Sprite(8, 10,bytearray([62,254,254,126,255,254,252,120,
            0,3,3,0,1,1,0,0]))]
            
            # BITMAP: width: 5, height: 6
demon6 = [thumby.Sprite(5, 6,bytearray([49,6,54,42,53])),
            thumby.Sprite(5, 6,bytearray([14,63,15,31,14]))]
            
# BITMAP: width: 34, height: 32
demon32B = [thumby.Sprite(34, 32,bytearray([255,255,127,127,127,191,175,47,31,27,19,195,231,231,240,225,199,15,7,189,191,111,127,255,255,255,255,255,255,255,255,255,255,255,
           128,126,127,39,131,247,247,243,241,0,12,216,216,217,213,245,180,118,119,205,121,53,143,224,100,49,25,123,119,111,111,223,191,127,
           255,255,255,255,255,255,255,15,241,224,192,7,15,143,207,247,247,7,198,242,120,248,224,6,31,255,255,254,254,254,224,237,239,224,
           255,255,255,255,255,191,159,175,54,113,127,63,128,135,143,63,31,7,24,28,15,31,7,24,62,127,255,255,255,255,255,255,255,255])),
           thumby.Sprite(34, 32,bytearray([0,0,128,128,128,192,208,208,224,228,236,252,248,248,255,254,248,240,248,194,192,144,128,0,0,0,0,0,0,0,0,0,0,0,
           127,255,255,255,127,15,15,15,15,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,252,248,240,240,224,192,128,
           0,0,0,0,0,0,0,240,254,255,255,255,255,127,63,15,15,255,255,255,255,255,255,249,224,0,0,1,1,1,31,31,31,31,
           0,0,0,0,0,64,96,112,249,255,255,255,127,120,112,192,224,248,255,255,255,255,255,231,193,128,0,0,0,0,0,0,0,0]))]
            
# BITMAP: width: 26, height: 24
demon24B = [thumby.Sprite(26, 24,bytearray([63,63,95,223,235,195,6,4,33,51,51,184,177,131,194,175,167,239,159,95,31,159,255,255,255,255,
           248,246,247,240,254,126,158,0,63,127,127,191,186,22,6,133,195,1,116,246,243,230,133,109,123,7,
           255,255,255,255,191,156,35,127,60,128,190,255,63,0,56,63,63,7,48,127,255,255,255,255,255,255])),
           thumby.Sprite(26, 24,bytearray([192,192,224,224,244,252,249,251,254,252,252,255,254,252,253,240,248,240,224,224,224,96,0,0,0,0,
           7,15,15,15,1,129,225,255,255,255,255,127,127,255,255,255,255,255,143,15,15,31,126,254,252,248,
           0,0,0,0,64,99,255,255,255,127,65,0,192,255,255,255,255,255,207,128,0,0,0,0,0,0]))]
           
           # BITMAP: width: 20, height: 18
demon18B = [thumby.Sprite(20, 18,bytearray([15,207,23,181,179,2,193,201,236,169,161,51,215,213,111,175,143,127,127,255,
           254,254,254,255,199,48,227,3,243,251,59,195,251,48,132,252,252,225,239,224,
           3,3,3,1,0,1,1,0,3,0,0,0,0,0,0,3,3,3,3,3])),
           thumby.Sprite(20, 18,bytearray([240,240,248,122,124,253,254,254,255,254,254,252,248,250,240,240,240,128,128,0,
           1,1,1,0,56,255,255,255,15,7,199,255,255,255,123,3,3,31,31,31,
           0,0,0,2,3,3,3,3,0,3,3,3,3,3,3,0,0,0,0,0]))]
           
          # BITMAP: width: 15, height: 14
demon14B = [thumby.Sprite(15, 14,bytearray([143,183,135,197,131,18,177,155,129,231,37,175,175,95,63,
           63,63,63,63,41,32,37,62,24,6,6,57,63,62,62])),
           thumby.Sprite(15, 14,bytearray([112,120,120,58,124,253,254,252,254,248,250,112,112,224,192,
           0,0,0,0,22,31,27,1,39,63,63,6,0,1,1]))]
           
       # BITMAP: width: 11, height: 10
demon10B = [thumby.Sprite(11, 10,bytearray([231,227,242,1,36,177,57,8,231,134,143,
           3,3,2,2,3,1,0,0,3,3,3])),
           thumby.Sprite(11, 10,bytearray([24,28,13,254,255,126,254,255,24,121,112,
            0,0,1,1,0,2,3,3,0,0,0]))]
           
           # BITMAP: width: 34, height: 13
demon32D = [thumby.Sprite(34, 13,bytearray([255,199,199,135,7,131,195,227,243,243,113,113,225,233,204,253,253,253,125,125,121,249,253,253,141,13,77,93,219,155,59,119,119,7,
            27,19,17,20,22,7,3,15,15,15,0,28,28,28,29,29,30,30,30,30,28,24,17,1,9,13,15,15,14,13,5,17,31,31])),
            thumby.Sprite(34, 13,bytearray([0,56,56,120,248,252,252,252,252,252,254,254,254,254,255,254,254,254,254,254,254,254,254,254,254,254,190,190,60,124,252,248,248,248,
            4,12,14,15,15,31,31,31,31,31,31,3,3,3,3,3,1,1,1,1,3,7,15,31,31,31,31,31,31,30,30,14,0,0]))]
            
       # BITMAP: width: 24, height: 9
demon24D = [thumby.Sprite(24, 9,bytearray([115,49,145,193,97,241,248,56,152,156,158,222,222,222,156,28,62,118,230,214,165,157,27,195,
            0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])  ),
            thumby.Sprite(24, 9,bytearray([140,206,238,254,254,254,255,255,127,127,127,63,63,63,127,255,255,255,255,239,222,254,252,60,
            1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0]))]
            
           # BITMAP: width: 16, height: 6
demon18D = [thumby.Sprite(16, 6,bytearray([57,9,17,25,25,8,10,46,46,46,14,30,25,17,3,51]) ),
               thumby.Sprite(16, 6,bytearray([6,54,62,62,62,63,63,31,31,31,63,63,62,62,60,12]))]
           
           
           # BITMAP: width: 11, height: 4
demon14D = [thumby.Sprite(11, 4,bytearray([12,0,4,4,6,2,6,6,4,0,12])),
                thumby.Sprite(11, 4,bytearray([3,15,15,15,15,15,15,15,15,15,3]))]
            
            
            # BITMAP: width: 11, height: 9
keyUI = [bytearray([124,135,153,149,29,53,61,53,61,1,255,
           0,0,0,1,1,1,1,1,1,1,0]),
           bytearray([124,255,255,255,255,255,255,255,255,255,255,
           0,0,0,1,1,1,1,1,1,1,0])]
           # BITMAP: width: 3, height: 2
pressUI = bytearray([1,3,1])
           
           # BITMAP: width: 37, height: 30
explosion = [thumby.Sprite(37, 30,bytearray([255,255,127,63,31,31,15,15,15,7,7,195,99,33,193,208,216,216,220,140,200,201,203,219,19,7,31,15,15,31,63,191,63,127,255,255,255,
           15,3,0,0,0,26,28,6,24,26,252,252,242,254,255,255,255,255,255,255,255,255,255,255,255,255,238,220,243,14,60,120,0,32,7,31,63,
           254,240,192,192,0,6,0,0,6,14,12,1,19,183,175,191,159,159,127,127,127,255,251,111,143,7,7,195,145,140,132,16,12,128,130,227,248,
           63,63,63,63,63,63,63,62,60,60,61,61,56,56,49,33,33,33,4,0,4,6,35,49,57,56,56,62,62,62,62,63,63,63,63,63,63])),
            thumby.Sprite(37, 30,bytearray([0,0,128,192,224,224,240,240,240,248,248,252,252,254,254,255,255,255,255,255,255,254,252,252,252,248,224,240,240,224,192,192,192,128,0,0,0,
           240,252,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,248,224,192,
           1,15,63,63,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,127,31,7,
           0,0,0,0,0,0,0,1,3,3,3,3,7,7,15,31,31,31,63,63,63,63,31,15,7,7,7,1,1,1,1,0,0,0,0,0,0]))]    

# BITMAP: width: 38, height: 33
explosion2 = [thumby.Sprite(38, 33,bytearray([255,255,255,255,255,255,143,79,87,247,243,250,249,243,247,231,234,199,199,198,74,73,75,139,203,199,11,23,39,111,159,223,127,127,255,255,255,255,
           127,255,47,15,243,248,250,252,252,11,243,255,251,251,223,15,207,107,155,184,233,225,241,100,229,239,224,224,131,112,99,7,191,56,232,119,31,255,
           255,207,117,2,17,129,156,252,193,50,77,23,23,135,179,255,236,110,252,104,242,239,207,121,112,127,115,115,255,191,247,255,39,140,224,153,195,255,
           255,255,254,255,255,255,229,224,192,192,181,192,38,112,100,96,96,161,163,191,31,159,31,28,252,140,208,224,226,151,215,229,220,239,240,251,255,255,
           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])),
           thumby.Sprite(38, 33,bytearray([0,0,0,0,0,160,240,240,184,248,252,253,254,254,249,250,255,255,255,255,255,254,252,244,244,248,244,236,216,240,224,224,128,128,0,0,0,0,
           128,0,208,248,252,255,253,255,255,255,255,255,255,255,255,255,63,159,255,223,31,31,15,159,31,31,255,255,255,143,159,255,255,255,247,136,224,0,
           0,48,139,255,238,254,255,255,255,205,179,239,239,255,207,255,255,145,19,151,253,240,240,246,255,255,255,255,255,255,255,255,255,127,31,230,252,8,
           0,0,1,3,3,15,31,31,63,63,74,63,217,143,191,191,255,127,127,127,255,127,255,255,63,127,63,31,31,107,107,123,63,28,15,4,0,0,
           0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))]
           # BITMAP: width: 24, height: 29
guyLeft = bytearray([255,15,3,1,1,0,4,4,142,6,14,6,138,130,2,128,0,0,0,1,1,3,15,255,
           63,0,0,192,224,7,7,7,207,159,31,187,187,31,31,31,223,207,15,232,224,0,0,63,
           252,240,128,119,207,255,255,127,127,127,103,111,111,103,127,127,127,255,255,207,119,128,240,252,
           31,31,31,30,28,25,23,23,15,15,13,13,13,13,15,15,23,23,25,28,30,31,31,31])
           # BITMAP: width: 24, height: 29
guyRight = bytearray([255,15,3,1,1,0,4,4,142,6,14,6,138,130,2,128,0,0,0,1,1,3,15,255,
           63,0,0,224,8,207,207,31,31,159,31,187,187,31,31,143,199,7,7,224,192,0,0,63,
           252,240,128,119,207,255,255,127,127,127,103,111,111,103,127,127,127,255,255,207,119,128,240,252,
           31,31,31,30,28,25,23,23,15,15,13,13,13,13,15,15,23,23,25,28,30,31,31,31])
           
           # BITMAP: width: 24, height: 29
guyHurt = bytearray([255,15,3,1,1,0,0,0,24,60,28,44,28,12,8,0,0,0,0,1,1,3,15,255,
           63,0,0,0,32,112,252,254,248,112,96,32,32,112,120,224,240,248,120,32,0,0,0,63,
           252,240,0,230,8,250,248,248,122,68,28,30,94,92,68,122,248,248,250,8,230,0,240,252,
           31,31,31,30,25,19,7,8,8,11,11,11,11,3,3,0,8,7,19,25,30,31,31,31])
           
# BITMAP: width: 24, height: 29
guyDie = bytearray([255,15,3,1,1,0,0,8,60,252,124,60,124,60,8,0,0,0,0,1,1,3,15,255,
           63,0,0,0,0,0,0,0,128,0,128,0,0,0,0,0,0,0,0,0,0,0,0,63,
           252,224,0,88,156,112,2,243,51,57,121,249,249,121,57,50,50,18,240,0,92,0,224,252,
           31,31,31,28,24,16,0,5,0,0,0,4,4,0,0,0,0,0,19,24,28,31,31,31])
           
# BITMAP: width: 16, height: 16
fireball =[thumby.Sprite(16, 16, bytearray([95,15,7,3,145,225,227,241,232,241,227,211,135,7,15,159,
           252,240,224,208,143,143,27,135,143,15,135,137,192,224,240,249])),
           thumby.Sprite(16, 16, bytearray([160,240,248,252,254,254,252,254,255,254,252,252,248,248,240,96,
           3,15,31,63,127,127,255,127,127,255,127,127,63,31,15,6]))]
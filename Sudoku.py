Board =['-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-',
        '-','-','-','-','-','-','-','-','-']
r = None
c = None
game_on = True
def display_board():
    global Board
    print(Board[0]+ "( 1)" + " | " + Board[1] + "( 2)" + " | " + Board[2] + "( 3)" + " | " + Board[3] + "( 4)" + " | " +Board[4]+ "( 5)" + " | " + Board[5] + "( 6)" + " | " +Board[6] + "( 7)"+ " | " + Board[7] + "( 8)"+ " | " +Board[8]+ "( 9)")
    print(Board[9]+ "(10)" + " | " + Board[10]+ "(11)" + " | " + Board[11]+ "(12)" + " | " + Board[12] + "(13)"+ " | " +Board[13] + "(14)" + " | " + Board[14] + "(15)"+ " | " +Board[15] + "(16)"+ " | " + Board[16]+ "(17)" + " | " +Board[17]+ "(18)")
    print(Board[18]+ "(19)" + " | " + Board[19]+ "(20)" + " | " + Board[20]+ "(21)" + " | " + Board[21]+ "(22)" + " | " +Board[22]+ "(23)" + " | " + Board[23]+ "(24)" + " | " +Board[24] + "(25)"+ " | " + Board[25]+ "(26)" + " | " +Board[26]+ "(27)")
    print(Board[27]+ "(28)" + " | " + Board[28] + "(29)"+ " | " + Board[29]+ "(30)" + " | " + Board[30] + "(31)" + " | " +Board[31] + "(32)" + " | " + Board[32]+ "(33)" + " | " +Board[33] + "(34)"+ " | " + Board[34] + "(35)"+ " | " +Board[35]+ "(36)")
    print(Board[36]+ "(37)" + " | " + Board[37]+ "(38)" + " | " + Board[38] + "(39)" + " | " + Board[39]+ "(40)" + " | " +Board[40] +  "(41)"+ " | " + Board[41] + "(42)"+ " | " +Board[42] + "(43)"+ " | " + Board[43] + "(44)"+ " | " +Board[44]+ "(45)")
    print(Board[45] + "(46)"+ " | " + Board[46]+ "(47)" + " | " + Board[47]+ "(48)" + " | " + Board[48]+ "(49)" + " | " +Board[49] + "(50)"+ " | " + Board[50] + "(51)"+ " | " +Board[51] + "(52)"+ " | " + Board[52]+ "(53)" + " | " +Board[53]+ "(54)")
    print(Board[54]+ "(55)" + " | " + Board[55]+ "(56)" + " | " + Board[56] + "(57)"+ " | " + Board[57]+ "(58)" + " | " +Board[58] + "(59)"+ " | " + Board[59] + "(60)" + " | " +Board[60] + "(61)" + " | " + Board[61]+ "(62)"  + " | " +Board[62 ]+ "(63)")
    print(Board[63]+ "(64)"  + " | " + Board[64]+ "(65)"  + " | " + Board[65]+ "(66)"  + " | " + Board[66] + "(67)" + " | " +Board[67]+ "(68)"  + " | " + Board[68]+ "(69)"  + " | " +Board[69] + "(70)"+ " | " + Board[70]+ "(71)" + " | " +Board[71]+ "(72)")
    print(Board[72]+ "(73)" + " | " + Board[73]+ "(74)" + " | " + Board[74]+ "(75)" + " | " + Board[75]+ "(76)" + " | " +Board[76]+ "(77)" + " | " + Board[77] + "(78)"+ " | " +Board[78] + "(79)"+ " | " + Board[79]+ "(80)" + " | " +Board[80]+ "(81)")


def input_game ():
    position = input ("select a position between 1 - 81 where you want to place the input :")
    while position not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50", "51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81"]:
        position = input ("place a valid input select a position between 1 - 81 where you want to place the input :")


    k = input ("Place a input you want to keep in "+ position +" : ")
    while k not in ["1","2","3","4","5","6","7","8","9"]:
        k = input ("Place a valid input you want to keep in "+ position +" position : ")
    position = int (position) - 1
    Board[position] = k
    display_board()

def check_rows ():
    global r
    row_1 = Board[0]!= Board[1]!= Board[2]!= Board[3] != Board[4] != Board[5] != Board[6] != Board[7] != Board[8] != '-'
    row_2 = Board[9]!= Board[10]!= Board[11]!= Board[12] != Board[13] != Board[14] != Board[15] != Board[16] != Board[17]!= '-'
    row_3 = Board[18]!= Board[19]!= Board[20]!= Board[21] != Board[22] != Board[23] != Board[24] != Board[25] != Board[26] != '-'
    row_4 = Board[27]!= Board[28]!= Board[29]!= Board[30] != Board[31] != Board[32] != Board[33] != Board[34] != Board[35] != '-'
    row_5 = Board[36]!= Board[37]!= Board[38]!= Board[39] != Board[40] != Board[41] != Board[42] != Board[43] != Board[44] != '-'
    row_6 = Board[45]!= Board[46]!= Board[47]!= Board[48] != Board[49] != Board[50] != Board[51] != Board[52] != Board[53] != '-'
    row_7 = Board[54]!= Board[55]!= Board[56]!= Board[57] != Board[58] != Board[59] != Board[60] != Board[61] != Board[62] != '-'
    row_8 = Board[63]!= Board[64]!= Board[65]!= Board[66] != Board[67] != Board[68] != Board[69] != Board[70] != Board[71] != '-'
    row_9 = Board[72]!= Board[73]!= Board[74]!= Board[75] != Board[76] != Board[77] != Board[78] != Board[79] != Board[80] != '-'
     
    if row_1 and row_2 and row_3 and row_4 and row_5 and row_6 and row_7 and row_8 and row_9 :
        r = True
    else :
        r = False
def check_columns():
    global c
    column_1 = Board[0]!= Board[9]!= Board[18]!= Board[27] != Board[36] != Board[45] != Board[54] != Board[63] != Board[72] != '-'
    column_2 = Board[1]!= Board[10]!= Board[19]!= Board[28] != Board[37] != Board[46] != Board[55] != Board[64] != Board[73]!= '-'
    column_3 = Board[2]!= Board[11]!= Board[20]!= Board[29] != Board[38] != Board[47] != Board[56] != Board[65] != Board[74] != '-'
    column_4 = Board[3]!= Board[12]!= Board[21]!= Board[30] != Board[39] != Board[48] != Board[57] != Board[66] != Board[75] != '-'
    column_5 = Board[4]!= Board[13]!= Board[22]!= Board[31] != Board[40] != Board[49] != Board[58] != Board[67] != Board[76] != '-'
    column_6 = Board[5]!= Board[14]!= Board[23]!= Board[32] != Board[41] != Board[50] != Board[59] != Board[68] != Board[77] != '-'
    column_7 = Board[6]!= Board[15]!= Board[24]!= Board[33] != Board[42] != Board[51] != Board[60] != Board[69] != Board[78] != '-'
    column_8 = Board[7]!= Board[16]!= Board[25]!= Board[34] != Board[43] != Board[52] != Board[61] != Board[70] != Board[79] != '-'
    column_9 = Board[8]!= Board[17]!= Board[26]!= Board[35] != Board[44] != Board[53] != Board[62] != Board[71] != Board[80] != '-'
    
    if column_1 and column_2 and column_3 and column_4 and column_5 and column_6 and column_7 and column_8 and column_9 :
        c = True
    else :
        c = False
      
def check_winner ():
    global r
    global c
    global game_on
    check_rows ()
    check_columns ()
    if r == True and c == True:
        game_on = False
        y = input ("congratulations you won the game. Type your name here :")
        print (y + "is our new champion")

def play_game ():
    display_board()
    while game_on:

        input_game ()
        check_winner ()


     
     
play_game()
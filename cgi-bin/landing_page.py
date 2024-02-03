

"""
.
.
.
.   LANDING/HOME PAGE
.
.
.
"""

print("Content-type:text/html\n\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Radovan Draskovic">
    
    <!-- mobile status bar color -->
    <meta name="theme-color" content="#fff">
    <title>Landing page</title>
    
    <!-- google font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Potta+One&display=swap" rel="stylesheet">
    
    <!-- box icons -->
    <link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
    
    <!-- app css -->
    <link rel="stylesheet" href="../styles/app.css">
    <link rel="shortcut icon" href="../images/icon.png" type="image/x-icon">
    
    <script src="../scripts/constant.js" defer></script>
    <script src="../scripts/sudoku.js" defer></script>
    <script src="../scripts/app.js" defer></script>
    <script src="../scripts/script.js" defer></script>
    
</head>

<body onload="prepare_page()">

    <!-- top nav -->
    <nav>
        <div class="nav-container">
            <span class="nav-logo">Sudoku</span>
            <span class="nav-logo-custom" onclick="logout_user()">Sign out</span>
            <div class="dark-mode-toggle" id="dark-mode-toggle">
                <i class="bx bxs-sun"></i>
                <i class="bx bxs-moon"></i>
            </div>
        </div>
    </nav>
    <!-- end top nav -->

    <div id="center-container">

        <!-- side bar -->
        <div id="side-nav-bar">
            <div id="div_image">
                <img src="../images/user_image.png" alt="user image" width=90 draggable="false">
            </div>
            <div class="user_info">
                <h2>User info</h2>
                <span>First name: </span> <span class="enter_from_database" id="input_result_from_db_firstName"></span> <br>
                <span>Last name: </span> <span class="enter_from_database" id="input_result_from_db_lastName"></span> <br>
                <span>Email: </span> <span class="enter_from_database" id="input_result_from_db_email"></span> <br>
                
                <table>
                    <tr class="has-line-above">
                        <th class="al-left">Total solved</th>
                        <th class="al-right" colspan=3;> <span class="enter_from_database" id="input_result_from_db_totalSolved"></span> </th>
                    </tr>
                    
                    <tr class="has-line-above">
                        <th class="al-left">Total points</th>
                        <th class="al-right" colspan=3;> <span class="enter_from_database" id="input_result_from_db_total_points"></span> </th>
                    </tr>
                    
                    <tr class="has-line-above">
                        <td class="al-left" rowspan=2;>Easy</td>
                        <td class="al-left">Solved:</td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_totalEasy"></span> </td>
                    </tr>
                    <tr>
                        <td>Best time: </td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_bestEasy"></span> </td>
                    </tr>

                    <tr class="has-line-above">
                        <td class="al-left" rowspan=2;>Medium</td>
                        <td class="al-left">Solved:</td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_totalMedium"></span> </td>
                    </tr>
                    
                    <tr>
                        <td>Best time: </td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_bestMedium"></span> </td>
                    </tr>
                    
                    <tr class="has-line-above">
                        <td class="al-left" rowspan=2;>Hard</td>
                        <td class="al-left">Solved:</td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_totalHard"></span> </td>
                    </tr>
                    <tr>
                        <td>Best time: </td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_bestHard"></span> </td>
                    </tr>
                    
                    <tr class="has-line-above">
                        <td class="al-left" rowspan=2;>Expert</td>
                        <td class="al-left">Solved:</td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_totalExpert"></span> </td>
                    </tr>
                    <tr>
                        <td>Best time: </td>
                        <td class="al-right"> <span class="enter_from_database" id="input_result_from_db_bestExpert"></span> </td>
                    </tr>
                    
                </table>
            </div>
        </div>
        <!-- end side bar -->

        <!-- main -->
        <div class="main">
            <div class="screen">
                <!-- start screen -->
                <div class="start-screen active" id="start-screen">
                    <span type="text" maxlength="11" class="input-name" id="input-name"></span>
                    <div class="btn" id="btn-level">
                        Easy
                    </div>
                    <div class="btn" id="btn-continue">Continue</div>
                    <div class="btn btn-blue" id="btn-play">New game</div>
                </div>
                <!-- end start screen -->

                <!-- game screen -->
                <div class="main-game" id="game-screen">
                    <div class="main-sudoku-grid">
                        <!-- 81 cells 9 x 9-->
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <div class="main-grid-cell"></div>
                        <!-- end 81 cells 9 x 9-->
                    </div>

                    <div class="main-game-info">
                        <div class="main-game-info-box main-game-info-name">
                            <span id="player-name"></span>
                        </div>
                        <div class="main-game-info-box main-game-info-level">
                            <span id="game-level">Easy</span>
                        </div>
                    </div>

                    <div class="main-game-info-box main-game-info-time">
                        <span id="game-time">00:00:00</span>
                        <div class="pause-btn" id="btn-pause">
                            <i class="bx bx-pause"></i>
                        </div>
                    </div>

                    <div class="numbers">
                        <div class="number">1</div>
                        <div class="number">2</div>
                        <div class="number">3</div>
                        <div class="number">4</div>
                        <div class="number">5</div>
                        <div class="number">6</div>
                        <div class="number">7</div>
                        <div class="number">8</div>
                        <div class="number">9</div>
                        <div class="delete" id="btn-delete">X</div>
                    </div>
                </div>
                <!-- end game screen -->

                <!-- pause screen -->
                <div class="pause-screen" id="pause-screen">
                    <div class="btn btn-blue" id="btn-resume">Resume</div>
                    <div class="btn" id="btn-new-game">New game</div>
                </div>
                <!-- end pause screen -->

                <!-- result screen -->
                <div class="result-screen" id="result-screen">
                    <div class="congrate">Completed</div>
                    <div class="info">Time</div>
                    <div id="result-time"></div>
                    <div class="btn" id="btn-new-game-2">New game</div>
                </div>
                <!-- end result screen -->
            </div>
        </div>
        <!-- end main -->
        
        <div id="leaderboards">
            <div id="div_image">
                <img src="../images/leaderboard_image.png" alt="leaderboard image" width=110 draggable="false">
            </div>
            <h2>Leaderboards</h2>
            <table id="leaderboards_table"></table>
        </div>
        
    </div>

</body>
    
</body>

"""
)
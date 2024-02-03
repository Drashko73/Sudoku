

// This regex pattern enforces a password to have a minimum length of 8 characters, including at least: 
//      one lowercase letter
//      one uppercase letter
//      one digit
//      one special character from the specified set (@$!%*?&_)
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,}$/;
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
const nameRegex = /^[a-zA-Z]+$/;

function check_email_address(email) { return emailRegex.test(email); }

function check_fistname(firstname) { return nameRegex.test(firstname); }

function check_lastname(lastname) { return nameRegex.test(lastname); }

function check_password(password) { return passwordRegex.test(password); }

/*  ********************************************************************
    GET COOKIE
    Function that gets cookie for the given name
    If cookie doesnt exist it returns null
    ******************************************************************** */
function getCookie(name) {
    const cookies = document.cookie.split(';');
    
    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.trim().split('=');
        if (cookieName === name) {
            return decodeURIComponent(cookieValue);
        }
    }
    return null;
}

/*  ********************************************************************
    IS ALREADY SIGNED IN
    If there is cookie sessid function checks whether the length is 14
    If everything is OK redirects user to landing page
    ******************************************************************** */
function is_already_signed_in() {
    
    if(getCookie('sessid')) {
        if(getCookie('sessid').length==14) {
            
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    window.location = 'http://localhost:8000/cgi-bin/landing_page.py';
                }
            };
            xmlhttp.open("GET", `../cgi-bin/requests.py?check_login=1&sessid=${getCookie('sessid')}`, true);
            xmlhttp.send();
        }
    }
}

/*  ********************************************************************
    CHECK IF IS SIGNED IN
    Checks whether there is signed in user
    If user is not signed in it is redirected to sign in page
    ******************************************************************** */
function check_if_is_signed_in() {

    let accept = false;
    if(getCookie('sessid') && getCookie('sessid').length==14) accept = true;

    if(accept == false) window.location = 'http://localhost:8000/cgi-bin/signin.py';
}

/*  ********************************************************************
    ENTER DATA
    Function that gets data from database and fills in user info fields
    ******************************************************************** */
function enter_data() {
    
    let firstName_field = document.getElementById("input_result_from_db_firstName");
    let lastName_field = document.getElementById("input_result_from_db_lastName");
    let email_field = document.getElementById("input_result_from_db_email");
    let totalSolved_field = document.getElementById("input_result_from_db_totalSolved");

    let totalEasy_field = document.getElementById("input_result_from_db_totalEasy");
    let totalMedium_field = document.getElementById("input_result_from_db_totalMedium");
    let totalHard_field = document.getElementById("input_result_from_db_totalHard");
    let totalExpert_field = document.getElementById("input_result_from_db_totalExpert");

    let bestEasy_field = document.getElementById("input_result_from_db_bestEasy");
    let bestMedium_field = document.getElementById("input_result_from_db_bestMedium");
    let bestHard_field = document.getElementById("input_result_from_db_bestHard");
    let bestExpert_field = document.getElementById("input_result_from_db_bestExpert");

    let total_points_field = document.getElementById("input_result_from_db_total_points");

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {

        if(this.readyState == 4 && this.status == 200) {

            response = JSON.parse(this.responseText);
            
            if (response != 'False') {
                firstName_field.innerHTML = response["firstName"];
                lastName_field.innerHTML = response["lastName"];
                email_field.innerHTML = response["email"];
                totalSolved_field.innerHTML = response["totalPlayed"];

                totalEasy_field.innerHTML = response["playedEasy"];
                totalMedium_field.innerHTML = response["playedMedium"];
                totalHard_field.innerHTML = response["playedHard"];
                totalExpert_field.innerHTML = response["playedExpert"];
                
                bestEasy_field.innerHTML = response["bestEasy"];
                bestMedium_field.innerHTML = response["bestMedium"];
                bestHard_field.innerHTML = response["bestHard"];
                bestExpert_field.innerHTML = response["bestExpert"];

                total_points_field.innerHTML = response["totalPoints"];
            }
        }
    }
    xmlhttp.open("GET",`../cgi-bin/requests.py?get_user_info=1&email=${getCookie("email")}`,true);
    xmlhttp.send();
}

/*  ********************************************************************
    CREATE LEADERBOARD
    Function that creates leaderboard table based on user's points
    ******************************************************************** */
function create_leaderboard() {

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {

        if(this.readyState == 4 && this.status == 200) {

            response = JSON.parse(this.responseText);
            
            if (response != 'False') {
                table_ref = document.getElementById("leaderboards_table");
                table_ref.innerHTML = "";

                let header_row = document.createElement("tr");
                    let th1 = document.createElement("th"); th1.innerHTML = "Rank";
                    let th2 = document.createElement("th"); th2.innerHTML = "First name";
                    let th3 = document.createElement("th"); th3.innerHTML = "Last name";
                    let th4 = document.createElement("th"); th4.innerHTML = "Points";

                    header_row.appendChild(th1);
                    header_row.appendChild(th2);
                    header_row.appendChild(th3);
                    header_row.appendChild(th4);

                table_ref.appendChild(header_row);

                let rank = 0;
                let last_points = -1;
                let skipping = 0;
                for (const user of response) {
                    let newRow = document.createElement("tr");

                    if(user["totalPoints"] != last_points) { rank = rank + 1 + skipping; skipping = 0; }
                    else skipping++;
                    last_points = user["totalPoints"];

                    let cname = "not_logged_in_user";
                    if(user["email"] == getCookie("email"))
                        cname = "logged_in_user";

                    let td1 = document.createElement("td"); td1.innerHTML = rank;                   td1.classList = cname;
                    let td2 = document.createElement("td"); td2.innerHTML = user["firstName"];      td2.classList = cname;
                    let td3 = document.createElement("td"); td3.innerHTML = user["lastName"];       td3.classList = cname;
                    let td4 = document.createElement("td"); td4.innerHTML = user["totalPoints"];    td4.classList = cname;

                    newRow.appendChild(td1);
                    newRow.appendChild(td2);
                    newRow.appendChild(td3);
                    newRow.appendChild(td4);

                    table_ref.appendChild(newRow);
                }
            }
        }
    }
    xmlhttp.open("GET",`../cgi-bin/requests.py?get_all_users=1`,true);
    xmlhttp.send();

}

/*  ********************************************************************
    PREPARE PAGE
    Function called on body load to:
        Check if there is an active sessid
        Enter user info on landing page if there is an active user
    ******************************************************************** */
function prepare_page() {
    check_if_is_signed_in();
    enter_data();
    create_leaderboard();
}

/*  ********************************************************************
    REGISTER USER
    Function called for registering new user
        Gets elements from input fields required for registering user
        Redirects user to landing page
    ******************************************************************** */
function register_user() {

    let first_name  = document.getElementById("input_firstname").value;
    let last_name   = document.getElementById("input_lastname").value;
    let email       = document.getElementById("input_email").value;
    let password    = document.getElementById("passwordInput").value;
    let agreement   = document.getElementById("agreement_terms");

    let errormsg = "";

    if(agreement.checked == false) {
        errormsg = "Agreement is required for creating an account <br>";
    }
    else {
        if(!check_fistname(first_name)) errormsg += "First name is not valid <br>";
        if(!check_lastname(last_name)) errormsg += "Last name is not valid <br>";
        if(!check_email_address(email)) errormsg += "Email is not valid <br>";
        if(!check_password(password)) errormsg += "Password is not valid";
    }

    if(errormsg == "") {
        register_info = {}
        register_info['firstName'] = first_name;
        register_info['lastName'] = last_name;
        register_info['email'] = email;
        register_info['password'] = password;
        register_info['balance'] = 0.0;
        register_info = JSON.stringify(register_info);

        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {

            if(this.readyState == 4 && this.status == 200) {

                response = JSON.parse(this.responseText);
                
                if (response['register'] == "True") {
                    alert("Success! You can sign in now!");
                    window.location = 'http://localhost:8000/cgi-bin/signin.py';
               }
               else if(response['register']=="False") {
                    document.querySelector("#error_msg_display").innerHTML='User with given email already exists!';
               }
            }
        }
        xmlhttp.open("GET",`../cgi-bin/requests.py?register_request=1&info=${register_info}`,true);
        xmlhttp.send();
    }
    else { // there is an error
        document.getElementById("error_msg_display").innerHTML = errormsg;
        return false;
    }
}

/*  ********************************************************************
    LOGIN USER
    Function called in order to login user
        Creates cookies required for logged in user
    ******************************************************************** */
function login_user() {
    let email = document.querySelector("#input_email").value;
    let password = document.querySelector("#passwordInput").value;

    if(email == "" || password == "")
        document.querySelector("#error_msg_display").innerHTML='Invalid credentials!';
    else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200) {
                response = JSON.parse(this.responseText);

                if (response['login'] == "True") {

                    const d = new Date();
                    d.setTime(d.getTime() + 3600000);
                    
                    // Delete old cookie
                    c = document.cookie.split(";");
                    for(i=0;i<c.length;i++) {
                        document.cookie = c[i] + "=; expires="+ new Date(0).toUTCString();
                    }

                    document.cookie = `sessid=${response["info"]['sessid']}; expires=${d.toUTCString()};`;
                    document.cookie = `email=${response["info"]['email']}; expires=${d.toUTCString()};`;
                    document.cookie = `firstName=${response["info"]['firstName']}; expires=${d.toUTCString()};`;
                    document.cookie = `lastName=${response["info"]['lastName']}; expires=${d.toUTCString()};`;
                    // document.cookie = `balance=${response["info"]['balance']}; expires=${d.toUTCString()};`;
                    window.location = 'http://localhost:8000/cgi-bin/landing_page.py';
                }
                else {
                    document.querySelector("#error_msg_display").innerHTML='User does not exist!';
                }
            }
        }
    }
    xmlhttp.open("GET",`../cgi-bin/requests.py?login_request=1&email=${email}&password=${password}`,true);
    xmlhttp.send();
}

/*  ********************************************************************
    LOGOUT USER
    Function called in order to logout user
        Deletes cookies that are stored for previously logged in user
        Redirects user to SIGN IN page
    ******************************************************************** */
function logout_user() {
    
    document.cookie = "email=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
	document.cookie = "firstName=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
	document.cookie = "lastName=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
    // document.cookie = "balance=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.cookie = "sessid=; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
            localStorage.removeItem("game");
            localStorage.removeItem("darkmode");
            localStorage.removeItem("player_name");
            window.location = 'http://localhost:8000/cgi-bin/signin.py';
        }
    };
    xmlhttp.open("GET", `../cgi-bin/requests.py?logout_request=1&sessid=${getCookie('sessid')}`, true);
    xmlhttp.send();
}

/*  ********************************************************************
    CLOSE PAGE
    Function used for closing page after button click
    ******************************************************************** */
function close_page() {
    window.close();
}
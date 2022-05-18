Mandatory password manager application functions/requirements:
    When an application open first time, a .csv or .txt file is created. A file must be encrypted with the AES algorithm when the application is shut down. The next time the system 
    is started, file is decrypted. (4 points) ✅
    Saving new password: fill the information form (title, password, URL/application, other information). All information is saved in a .csv or .txt file. The password encrypt with 
    algorithm (AES, DES, RSA). You can choose which algorithm to use. (3 points) ✅
    Search password by title. (2 points) ✅
    Update password by title. New password encrypt with the same algorithm. (2 points). ✅
    Delete password function. All information about password is delete from file. (2 points) ✅

Optional password manager application functions:
    Create registration and login forms (username, password). User password must be encrypted (choose encrypted method PBKDF2, Bcrypt, Scrypt, Argon2 or hash function). Assign a 
    .csv or .txt file to a new user. It is mean modify first mandatory requirement. (3 points) ✅
    When the user login to the account the file is decrypted. The file is encrypted when user log out or the application crashes. (3 points) ✅
    Create random password generator function. (2 points) ✅
    Extra function for password search by title: when the password is found it is not show immediately. To show encrypted password. Press the "Show" button and see decrypted 
    password. (2 points) 
    Create button that can copy the password to the clipboard. (2 points) ✅
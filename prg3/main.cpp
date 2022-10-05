
#include "Biob.h"
#include "Csci.h"
#include "Egen.h"
#include "Semester.h"
//

void Menu(Semester s){
    //var holding selection
    char selc;
    int sel;

    //print options
    printf("Choices: \n"
           "n - print class given number\n"
           "t - print all class for a given type\n"
           "q - quit\n");
    cin >> selc;
    //switch statement
    //convert entry into int containing asci value
    sel = (int)(selc);
    //if selection = q exit
    if(sel == 113){
        return;
    }
    switch(sel){
        //110 = n
        case 110 :
            //discard char from menu
            getchar();

            s.print_by_number();

            break;
            //116 = t
        case 116 :
            string type;
            cout << "Enter Type of Class (CSCI, EGEN, or BIOB): ";
            cin >> type;
            s.print_by_type(type);
            break;

    }
    Menu(s);
    return;
}

int main (void) {
    
    Semester s;

    //open file
    s.read();
    //s.read2();
    //print by type test
    //s.print_by_type("CSCI");
    //print by number test
    //s.print_by_number();


    //run menu until exit
    Menu(s);
    return(0);
}

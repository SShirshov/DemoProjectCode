//semester class
#ifndef SEMESTER_H
#define SEMESTER_H
#include "Biob.h"
#include "Csci.h"
#include "Egen.h"
#include <fstream>
#include <vector>
#include<iostream>
#include<iomanip>
#include <string>
#include <sstream>

using namespace std;

class Semester{
    private:
        //vectors of classes
        vector<Biob> biob;
        vector<Csci> csci;
        vector<Egen> egen;
        //classes
        Biob B;
        Csci C;
        Egen E;

    public:
        void setc(string t[], string typ){
            //set if csci
            if (typ == "CSCI"){
                //set type
                C.setCtype(t[0]);
                //set num
                C.setCnum(t[1]);
                //set title
                C.setCtitle(t[2]);
                //set profesor
                C.setCprof(t[3]);
                //push vector back
                csci.push_back(C);
            }
            //set if EGEN
            else if (typ == "EGEN"){
                E.setCtype(t[0]);
                E.setCnum(t[1]);
                E.setCtitle(t[2]);
                E.setCprof(t[3]);
                egen.push_back(E);
            }
            //set if BIOB
            else if (typ == "BIOB"){
                B.setCtype(t[0]);
                B.setCnum(t[1]);
                B.setCtitle(t[2]);
                B.setCprof(t[3]);
                biob.push_back(B);
            }
        }

        void read() {
            string typ;
            string line;
            string array[4];
            ifstream file("/Users/simeonshirshov/Desktop/DM/prg3/classes.csv");
            if (file.is_open()) {
                while (getline(file, line)) {   // read line
                    stringstream ss(line);
                    //go through line pulling each value
                    for (int cn = 0; cn < 4; cn++) {
                        //cout << cn;

                        if (cn == 0) {
                            //parse first value with space as dilimeter
                            getline(ss, typ, ' ');
                            //cout << typ << endl; /* for debug*/
                            //set type as the first value parsed
                            array[cn] = typ;

                        } else {
                            //parse the rest with "," delimiter
                            getline(ss, line, ',');
                            //cout << line << endl; /* for debug*/
                            array[cn] = line;
                        }
                    }
                    //enter line (class) into correct class
                    setc(array, typ);
                }
            }
        }

        void print_by_type(string t){
            if (t == "CSCI"){
                for(int i=0; i < (int)csci.size(); i++){
                    csci[i].print();
                }
            }
            else if (t == "EGEN"){
                for(int i=0; i < (int)egen.size(); i++){
                    egen[i].print();
                }
            }
            else if (t == "BIOB"){
                for(int i=0; i < (int)biob.size(); i++){
                    biob[i].print();
                }
            }
        }

        void print_by_number(){
            string input, input2, input3;
            cout << "Enter class type and class number (ex: CSCI 112) : ";
            //read in line
            getline(cin, input);
            istringstream in (input);
            //break apart type and number
            in >> input2 >> input3;
            //cout << "\n"<<input2 << input3 <<endl; /*debug*/
            //choose vector
            if (input2 == "CSCI"){
                //find correct class
                for(int i=0; i < (int)csci.size(); i++){
                    if(csci[i].getCnum() == input3){
                        //print class
                        csci[i].print();
                    }
                }
            }
            else if (input2 == "BIOB"){
                for(int i=0; i < (int)biob.size(); i++){
                    if(biob[i].getCnum() == input3){
                        biob[i].print();
                    }
                }
            }
            else if (input2 == "EGEN"){
                for(int i=0; i < (int)egen.size(); i++){
                    if(egen[i].getCnum() == input3){
                        egen[i].print();
                    }
                }
            }
            else{
                cout << "\nFalse Entry\n";
            }
        }

};
#endif /* SEMESTER_H */

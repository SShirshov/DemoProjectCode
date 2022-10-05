//CSCI class
#ifndef CSCI_H
#define CSCI_H
#include "University.h"

#include<iostream>
#include <string>
using namespace std;

class Csci : public University{


    public:
        //pri nt csci
        void print() {
            cout << getCtype() << " - " << getCtitle() << " - " << getCnum() << " - " << getCprof() << endl;
        }

};
#endif /* CSCI_H */

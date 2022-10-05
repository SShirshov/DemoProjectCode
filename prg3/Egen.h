//EGEN Class

#ifndef EGEN_H
#define EGEN_H
#include "University.h"

#include<iostream>
#include <string>
using namespace std;

class Egen : public University{

    public:
        //print egen
        void print() {
            cout << getCtype() << " - " << getCprof() << " - " << getCtitle() << " - " << getCnum() << endl;
        }

};

#endif /* EGEN_H */

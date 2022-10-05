//BIOB Class

#ifndef BIOB_H
#define BIOB_H
#include "University.h"

#include<iostream>
#include <string>
using namespace std;

class Biob : public University{

    public:
        //print biob
        void print() {
            cout << getCtype() << " - " << getCnum() << " - " << getCtitle() << " - " << getCprof() << endl;
        }
};


#endif /* BIOB_H */

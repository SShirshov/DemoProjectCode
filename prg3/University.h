//university class

#ifndef UNIVERSITY_H
#define UNIVERSITY_H
#include <string> 
using namespace std;

class University{
    private:
        string ctype;
        string cnum;
        string ctitle;
        string cprof;

    public:

        University() : ctype{"none"}, cnum{"none"}, ctitle{"none"}, cprof{"none"} {}//inline funtion

        University(string type, string num, string title, string prof)
        : ctype{type}, cnum{num}, ctitle{title}, cprof{prof} {};
        void set(string, string, string, string);

    //setters
       void setCtype(string type){ctype = type;}

       void setCnum(string num){cnum = num;}

       void setCtitle(string title){ctitle = title;}

       void setCprof(string prof){cprof = prof;}

       //getters
       string getCtype(){return ctype;}

       string getCnum(){return cnum;}

       string getCtitle(){return ctitle;}

       string getCprof(){return cprof;}


};
#endif /* UNIVERISTY_H */

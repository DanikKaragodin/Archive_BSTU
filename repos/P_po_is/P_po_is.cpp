
#include <iostream>
#include <iomanip>
using namespace std;

class Student {
private:
    int age;
    double score;
    char name[64];
public:
    Student() { this->age = 0; this->score = 0; strcpy_s(this->name, "Noname"); }
    Student(int age, double score, const char* name) {
        this->age = age;
        this->score = score;
        strcpy_s(this->name, name);
    }
    Student(Student& st2) {
        this->age = st2.age;
        this->score = st2.score;
        strcpy_s(this->name, st2.name);
    }
    void To_Set(int age, float score, const char* name)
    {
        this->age = age;
        this->score = score;
        strcpy_s(this->name, name);
    }
    void To_Show()
    {
        cout << setw(-20) << "Age of student: " << age << endl;
        cout << setw(-20) << "Academic score: " << score << endl;
        cout << setw(-20) << "His Name and Surname: "; puts(name);
        cout << endl;
    }
    int GetAge() { return this->age; }
    float GetScore() { return this->score; }
    char* GetName() { return this->name; }
    friend double operator-(Student& first, Student& second) {
        return first.score -= second.score;
    }
    double operator+(double up) { return this->score += up; }
    friend bool operator==(Student& first, Student& second) {
        return !strcmp(first.name, second.name);
    }
    short IsBetter(Student& st1) {
        if (st1.score < score) return 1;
        else return -1;
    }
    short IsBetter(Student& st1, Student& st2) {
        short promo = 0;
        if (st1.score < score) promo++;
        else promo--;
        if (st2.score < score) promo++;
        else promo--;
        return promo;
    }
    short IsBetter(Student& st1, Student& st2, Student& st3) {
        short promo = 0;
        if (st1.score < score) promo++;
        else promo--;
        if (st2.score < score) promo++;
        else promo--;
        if (st3.score < score) promo++;
        else promo--;
        return promo;
    }
};
class Vector {
private:
    double x, y, z;
    string real_or_no;
public:
    Vector() {
        this->x = 0;
        this->y = 0;
        this->z = 0;
        this->real_or_no = "false";
    }
    Vector(double x, double y, double z, string real_or_no = "true") {
        this->x = x;
        this->y = y;
        this->z = z;
        this->real_or_no = real_or_no;
    }
    Vector(const Vector& v2) {
        this->x = v2.x;
        this->y = v2.y;
        this->z = v2.z;
        this->real_or_no = v2.real_or_no;
    }
    void Set(double x, double y, double z, string real_or_no = "true") {
        this->x = x;
        this->y = y;
        this->z = z;
        this->real_or_no = real_or_no;
    }
    void Show() {
        setprecision(3);
        cout << "First coordinate(X): " << x << endl;
        cout << "Second coordinate(Y): " << y << endl;
        cout << "Third coordinate(Z): " << z << endl;
        cout << "He is real?: " << real_or_no << endl << endl;
        setprecision(6);
    }
    double GetX() { return this->x; }
    double GetY() { return this->y; }
    double GetZ() { return this->z; }
    string GetRoN() { return this->real_or_no; }
    friend Vector operator+(Vector& V1, Vector& V2) {
        return Vector(V1.x + V2.x, V1.y + V2.y, V1.z + V2.z);
    }
    Vector operator-(double d) {
        return Vector(this->x - d, this->y - d, this->z - d);
    }
    friend double operator*(Vector& V1, Vector& V2) {
        return (V1.x * V2.x + V1.y * V2.y + V1.z * V2.z);
    }
    double Skalyar_myltiply(Vector& V1) {
        return (V1.x * this->x + V1.y * this->y + V1.z * this->z);
    }
    double Skalyar_myltiply(Vector& V1, Vector& V2) {
        return (V1.x * this->x * V2.x + V1.y * this->y * V2.y + V1.z * this->z * V2.z);
    }
    double Skalyar_myltiply(Vector& V1,Vector& V2,Vector& V3) {
        return (V1.x * this->x * V2.x * V3.x + V1.y * this->y * V2.y * V3.y + V1.z * this->z * V2.z * V3.z);
    }
};
class Character {
private:
    short id,health;
    string name;
public:
    Character() {
        id = -1;
        name = "Andrey Puchinky";
        health = 10;
    }
    Character(short id, string& name, short health) {
        this->id = id;
        this->name = name;
        this->health = health;
    }
    Character(const Character& ch){
        this->id = ch.id;
        this->name = ch.name;
        this->health = ch.health;
    }
    void Set(short id = -1, string name = "Andrey Puchinky", short health = 10) {
        this->id = id;
        this->name = name;
        this->health = health;
    }
    void Show() {
        cout << "Id: " << id << endl
            << "Name: " << name << endl
            <<"Health: " << health << endl;
    }
    short GetId() { return id; }
    string GetName() { return name; }
    short GetHealth() { return health; }
    friend bool operator==(Character& ch1, Character& ch2) {
        if (ch1.id == ch2.id) return true;
        else return false;
    }
    short operator-(short damage) {
        this->health -= damage;
        return this->health;
    }
    short operator+(short health) {
        this->health += health;
        return this->health;
    }
    short medic(Character& ch1) {
        ch1.health += 10;
        health -= 5;
    }
    short medic(Character& ch1, Character& ch2) {
        ch1.health += 10;
        ch2.health += 10;
        health -= 10;
    }
    short medic(Character& ch1, Character& ch2, Character& ch3) {
        ch1.health += 10;
        ch2.health += 10;
        ch3.health += 10;
        health -= 15;
    }
};
int main()
{
    return 228;
}

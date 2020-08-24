#include "System.hpp"

System::System(unsigned int idx, std::string n, float x, float y, float z, bool hs){
	//Initialize identifiers
	this->name = n;
	this->idx = idx;

	//Initialize coordinates
	this->coords[0] = x;
	this->coords[1] = y;
	this->coords[2] = z;

	this->has_station = hs;
}

System::~System(){
}

//Setters
void System::addLink(System* s){
	this->links.push_back(s);
}

//Getters
std::vector<System*> System::getLinks(){
	return this->links;
}

unsigned int System::getIdx(){
	return this->idx;
}

std::string System::getName(){
	return this->name;
}

float* System::getCoords(){
	return this->coords;
}

bool System::hasStation(){
	return this->has_station;
}

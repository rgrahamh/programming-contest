#ifndef IPS_H
#define IPS_H

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <math.h>
#include "../System/System.hpp"

//Final path tracking info
typedef struct routing {
	float total_dist = 0.0;
	std::vector<System*> valid_path;
} pathfinder;

//Max ship range and destination
float max_range = 0.0;
unsigned int dest_idx;

//The system map
std::vector<System*> systems;

//Function declaration
float getDist(System* sys1, System* sys2);
pathfinder* findPath(unsigned int curr_idx, std::vector<System*>* curr_path, float fuel_left, float total_dist);

#endif

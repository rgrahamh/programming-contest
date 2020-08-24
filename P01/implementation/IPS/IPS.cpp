#include "IPS.hpp"

float getDist(System* sys1, System* sys2){
	//Get coordinates
	float* coords1 = sys1->getCoords();
	float* coords2 = sys2->getCoords();

	//Calculate differences
	float xDiff = abs(coords1[0] - coords2[0]);
	float yDiff = abs(coords1[1] - coords2[1]);
	float zDiff = abs(coords1[2] - coords2[2]);

	//Get the length of the first segemnet (pythag between X and Y)
	float seg1 = sqrt(pow(xDiff, 2) + pow(yDiff, 2));

	//Return the total 3D distance (pythag between seg1 and Z)
	return sqrt(pow(seg1, 2) + pow(zDiff, 2));
}

pathfinder* findPath(unsigned int curr_idx, std::vector<System*> curr_path, float fuel_left, float total_dist){
	//If we've already visited a planet in this system, it's not valid.
	System* system = systems[curr_idx];
	for(unsigned long int i = 0; i < curr_path.size(); i++){
		if(curr_path[i] == system){
			return NULL;
		}
	}

	//Add to the path list
	curr_path.push_back(system);

	//Checking if this is the destination
	if(dest_idx == curr_idx){
		//Make a new path, init to current values
		pathfinder* path = new pathfinder();
		path->total_dist = total_dist;
		path->valid_path = curr_path;

		//Pop self off the list
		curr_path.pop_back();

		return path;
	}

	//Refill at a station (if one is present)
	if(system->hasStation()){
		fuel_left = max_range;
	}

	//Get all systems within max jump range
	std::vector<System*> adj_systems = system->getLinks();

	pathfinder* best_path = NULL;
	for(unsigned long int i = 0; i < adj_systems.size(); i++){
		//Get the next system
		System* next_system = adj_systems[i];

		//Calculate flight distance
		float dist = getDist(system, next_system);
		//If we can make the jump
		if(fuel_left >= dist){
			//Simulate making the jump
			pathfinder* new_path = findPath(next_system->getIdx(), curr_path, fuel_left - dist, total_dist + dist);

			//If the new path is better than the current best path, change the best path
			if(best_path == NULL){
				best_path = new_path;
			}
			else if(new_path != NULL && new_path->total_dist < best_path->total_dist){
				delete best_path;
				best_path = new_path;
			}
			else if(new_path != NULL){
				delete new_path;
			}
		}
	}

	//Pop self off the list
	curr_path.pop_back();

	return best_path;
}

int main(int argc, char** argv){
	std::string start = "";
	std::string dest = "";

	//First line of input
	std::cin >> start;
	std::cin >> dest;
	std::cin >> max_range;

	//Loop vars
	std::string name = "";
	float coord1;
	float coord2;
	float coord3;
	bool has_station;
	unsigned int idx = 0;
	unsigned int start_idx = 0;

	//The read has to happen first to check for the EOF
	std::cin >> name;
	while(!std::cin.eof()){
		//Getting the rest of the input for the system
		std::cin >> coord1;
		std::cin >> coord2;
		std::cin >> coord3;
		std::cin >> has_station; 

		//Create the new system
		System* new_system = new System(idx, name, coord1, coord2, coord3, has_station);

		//Initialize the starting node as the first thing in the path
		if(start.compare(name) == 0){
			start_idx = idx;
		}
		else if(dest.compare(name) == 0){
			dest_idx = idx;
		}
		//Create links between the current station and all other stations (within one tank's range)
		for(unsigned long int i = 0; i < systems.size(); i++){
			//Printing distance information (useful for building tests)
			//std::cout << "From " << systems[i]->getName() << " to " << new_system->getName() << " is " << getDist(new_system, systems[i]) << " lightyears" << std::endl;

			if(getDist(new_system, systems[i]) <= max_range){
				new_system->addLink(systems[i]);
				systems[i]->addLink(new_system);
			}
		}
		systems.push_back(new_system);

		idx++;
		std::cin >> name;
	}

	std::vector<System*> search_path;
	//Start the recustive solution
	pathfinder* best_path = findPath(start_idx, search_path, max_range, 0.0);

	//Outputting results
	if(best_path == NULL){
		std::cout << "No Valid Route" << std::endl;

		//Final free
		for(unsigned long int i = 0; i < systems.size(); i++){
			delete systems[i];
		}
		delete best_path;

		return -1;
	} else {
		std::cout << std::fixed;
		std::cout << std::setprecision(4);
		std::cout << best_path->total_dist << std::endl;
		for(unsigned long int i = 0; i < best_path->valid_path.size(); i++){
			std::cout << best_path->valid_path[i]->getName() << std::endl;
		}

		//Final free
		for(unsigned long int i = 0; i < systems.size(); i++){
			delete systems[i];
		}
		delete best_path;

		return 0;
	}
}

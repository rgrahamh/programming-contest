//Changed it since system.h would be a popular file name ;P
#ifndef IPS_SYSTEM_H
#define IPS_SYSTEM_H

#include <stdlib.h>
#include <string>
#include <vector>

class System {
	private:
		std::vector<System*> links;
		std::string name;
		float coords[3];
		bool has_station;
		unsigned int idx;

	public:
		System(unsigned int idx, std::string n, float x, float y, float z, bool hs);
		~System();

		//Setters
		void addLink(System* s);

		//Getters
		std::vector<System*> getLinks();
		std::string getName();
		unsigned int getIdx();
		float* getCoords();
		bool hasStation();
};

#endif

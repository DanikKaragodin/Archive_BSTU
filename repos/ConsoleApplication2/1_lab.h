#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
class Graphs
{
public:
	struct graph_struct { short first; short second; };
	vector<graph_struct> graph;
	short max;
	Graphs();
	Graphs(string fileName);
	Graphs(Graphs& gh);
	~Graphs();
	void Out();
};
vector<vector<bool>> matrix_adj(Graphs& gh, bool output);
void matrix_incid(Graphs& gh);
void find_in_deep(Graphs& gh);
void find_in_weight(Graphs& gh);
#include "1_lab.h"
using namespace std;

	Graphs::Graphs() {
		max = 0;
	}
	Graphs::Graphs(string fileName) {
		ifstream ifs(fileName);
		size_t i = 0;
		ifs >> max;
		while (!ifs.eof()) {
			short first, second;
			ifs >> first >> second;
			graph.push_back({ first, second });
			i++;
		}
		ifs.close();
	};
	Graphs::Graphs(Graphs& gh) {
		graph = gh.graph;
		max = gh.max;
	}
	Graphs::~Graphs() { cout << "No Graphs :(" << endl; }
	void Graphs::Out() {
		for (auto i : graph)
			cout << i.first << "->" << i.second << endl;
		cout << endl;
	}

vector<vector<bool>> matrix_adj(Graphs& gh, bool output = false) {
	short max = gh.max;
	vector<vector<bool>> adj(max, vector<bool>(max, false));
	for (size_t i = 0; i < max; i++) {
		for (size_t j = 0; j < max; j++) {
			for (size_t k = 0; k < gh.graph.size(); k++) {
				if ((gh.graph.at(k).first - 1 == i && gh.graph.at(k).second - 1 == j)
					|| (gh.graph.at(k).first - 1 == j && gh.graph.at(k).second - 1 == i)) {
					adj[i][j] = true;
					break;
				}
			}
		}
	}
	if (output) {
		cout << " ";
		for (size_t i = 0; i < max; i++) cout << " " << i + 1;
		for (size_t i = 0; i < max; i++) {
			cout << endl << i + 1 << "|";
			for (size_t j = 0; j < max; j++) cout << adj[i][j] << " ";
		}
		cout << endl;
	}
	return adj;
}
void matrix_incid(Graphs& gh) {
	short max = gh.max;
	vector<vector<bool>> inc(gh.graph.size(), vector<bool>(max, false));
	for (size_t i = 0; i < gh.graph.size(); i++) {
		for (size_t j = 0; j < max; j++) {
			if (gh.graph.at(i).first - 1 == j || gh.graph.at(i).second - 1 == j) {
				inc[i][j] = true;
			}
		}
	}
	cout << "  ";
	for (size_t i = 0; i < max; i++)
	{
		cout << " " << i + 1;
	}
	for (size_t i = 0; i < gh.graph.size(); i++)
	{
		cout << endl << gh.graph.at(i).first << gh.graph.at(i).second << "|";
		for (size_t j = 0; j < max; j++)
		{
			cout << inc[i][j] << " ";
		}
	}
	cout << endl;
}
void find_in_deep(Graphs& gh) {
	short global_component = 0, max = gh.max, i = 0;
	bool all_visited = false;
	vector<bool> visited(max, false);
	vector<vector<bool>> mat_adj = matrix_adj(gh);
	stack<short> stack;
	for (short j = 0; j < max; j++) {
		if (visited[j]) continue;
		else {
			stack.push(j);
			all_visited = false;
			i = j;
			visited[i] = true;
		}
		while (!all_visited) {
			size_t st = stack.size();
			for (short k = 0; k < max; k++) {
				if (mat_adj[i][k] && !visited[k]) {
					stack.push(k); visited[k] = true;
					break;
				}
			}
			if (stack.size() == st) stack.pop();
			if (!stack.empty()) i = stack.top();
			all_visited = stack.empty();
		}
		++global_component;
	}
	cout << "Global_Copmonent: " << global_component << endl;
}
void find_in_weight(Graphs& gh) {
	short global_component = 0, max = gh.max, i = 0;
	bool all_visited = false;
	vector<bool> visited(max, false);
	vector<vector<bool>>mat_adj = matrix_adj(gh);
	stack<short> stack;
	for (short j = 0; j < max; j++) {
		if (visited[j]) continue;
		else {
			stack.push(j);
			all_visited = false;
			i = j;
			visited[i] = true;
		}
		while (!all_visited) {
			size_t st = stack.size();
			for (short k = 0; k < max; k++) {
				if (mat_adj[i][k] && !visited[k]) {
					stack.push(k); visited[k] = true;
				}
			}
			if (stack.size() == st) stack.pop();
			if (!stack.empty()) i = stack.top();
			all_visited = stack.empty();
		}
		++global_component;
	}
	cout << "Global_Copmonent: " << global_component << endl;
}
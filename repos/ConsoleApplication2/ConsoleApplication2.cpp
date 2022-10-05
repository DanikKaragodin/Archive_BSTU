#include "1_lab.h"
bool elier_if(Graphs& gh) {
	vector<vector<bool>> adj=matrix_adj(gh, true);
	short count;
	for (size_t i = 0; i < gh.max; i++)
	{
		count = 0;
		for (size_t j = 0; j < gh.max; j++) if (adj[i][j]) count++;
		if (!count % 2) { cout << "Incompatible graph"<<endl; return false; }
	}
	cout << "Compatible graph"<<endl;
	return true;
}
void elier_path(Graphs& gh) {
	vector<vector<bool>> adj = matrix_adj(gh,false);
	stack<short> st;
	short i = gh.graph[0].first-1;
	st.push(i+1);
	bool flag;
	while (true) { 
		flag = false;
		for (size_t j = 0; j < gh.max; j++)
		{if (adj[i][j]) {
			adj[i][j] = 0; adj[j][i] = 0;
			st.push(j+1);
			i = j;
			flag = true;
			break;
		}}
		if (flag) continue;
		cout << st.top();
		st.pop();
		if (!st.empty()) cout << "->";
		else { cout << endl; break; }
	}
}
void gamil_cycle(Graphs& gh) {
	short max = gh.max, i = 0;
	bool all_visited = false;
	vector<bool> visited(max, false);
	vector<vector<bool>> mat_adj = matrix_adj(gh,true);
	stack<short> stack;
	visited[i] = true;
		while (!all_visited) {
			size_t st = stack.size();
			for (short k = 0; k < max; k++) {
				if (mat_adj[i][k] && !visited[k]) {
					stack.push(k);
					visited[k] = true;
					break;
				}
			}
			if (stack.size() == st) {

				if (stack.size() + 1 == max && mat_adj[i][0]) {
					for (size_t j = 0; j < stack.size(); j++)
					{
						cout << stack.top() << "->";
					}
					cout << i + 1 << endl;
					return;
				}
				stack.pop(); }
			if (!stack.empty()) i = stack.top();
			all_visited = stack.empty();
		}
		cout << "cycle not be" << endl;
}
int main() {
	Graphs gh("graph1.txt");
	gh.Out();
	Graphs gh2("graph2.txt");
	gh2.Out();
	gamil_cycle(gh2);
	//if (elier_if(gh)) elier_path(gh);
	return 228;
}
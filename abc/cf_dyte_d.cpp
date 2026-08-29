#include <iostream>
#include <vector>
#include <algorithm>

constexpr long long INF = (1LL << 60);

// ワーシャルフロイド法 (1.1 基本実装)
// 負閉路が存在する場合 true を返す
bool FloydWarshall(std::vector<std::vector<long long>>& distances)
{
	const size_t v = distances.size();

	for (size_t i = 0; i < v; ++i)
	{
		for (size_t from = 0; from < v; ++from)
		{
			for (size_t to = 0; to < v; ++to)
			{
				if ((distances[from][i] < INF) && (distances[i][to] < INF))
				{
					distances[from][to] = std::min(distances[from][to], (distances[from][i] + distances[i][to]));
				}
			}
		}
	}

	for (size_t i = 0; i < v; ++i)
	{
		// 負閉路が含まれている場合, distances[i][i] が負になるような i が存在する
		if (distances[i][i] < 0)
		{
			return true;
		}
	}

	return false;
}

int main()
{
	int V, E;
	std::cin >> V >> E;

	std::vector<std::vector<long long>> distances(V, std::vector<long long>(V, INF));

	for (int i = 0; i < E; ++i)
	{
		int s, t, d;
		std::cin >> s >> t >> d;
		distances[s][t] = d;
	}

	for (int i = 0; i < V; ++i)
	{
		distances[i][i] = 0;
	}

	if (FloydWarshall(distances))
	{
		std::cout << "NEGATIVE CYCLE\n";
		return 0;
	}

	for (int from = 0; from < V; ++from)
	{
		for (int to = 0; to < V; ++to)
		{
			if (INF == distances[from][to])
			{
				std::cout << "INF";
			}
			else
			{
				std::cout << distances[from][to];
			}

			if (to != (V - 1))
			{
				std::cout << ' ';
			}
		}

		std::cout << '\n';
	}
}
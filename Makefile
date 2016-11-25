CXX=g++ -std=c++11

appPE: appPE.o main.o
	$(CXX) main.cpp appPE.cpp -o build_products/appPE -static-libstdc++ 

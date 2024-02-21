from RN import *

def main():
    a = RN("../../source_file/gdansk/roads.shp")
    a.move_points_to_road_network(["../../source_file/gdansk/households.shp"])

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'now_loation.dart';
import 'range.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 24, 149, 1),
        title: Text(
          "VISTA",
        ),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 50.0),
            child: Image.asset(
              'assets/vista.png',
              width: 280,
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 70.0),
            child: Column(
              children: [
                Center(
                  child: ElevatedButton(
                    style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(
                            const Color.fromARGB(255, 24, 149, 1)),
                        fixedSize: MaterialStateProperty.all<Size>(
                            Size(270, 90)) // 원하는 색상으로 변경
                        ),
                    child: Text("환자 현재 위치",
                        style: TextStyle(color: Colors.white, fontSize: 25)),
                    onPressed: () {
                      // 페이지 이동
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => NowLocation()),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
          SizedBox(height: 45),
          Center(
            child: ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => Range()),
                  );
                },
                style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all<Color>(
                        const Color.fromARGB(255, 24, 149, 1)),
                    fixedSize: MaterialStateProperty.all<Size>(
                        Size(270, 90)) // 원하는 색상으로 변경
                    ),
                child: Text("환자 위치 지정",
                    style: TextStyle(color: Colors.white, fontSize: 25))),
          ),
          SizedBox(height: 45),
          Center(
            child: ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => Anticipated()),
                  );
                },
                style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all<Color>(
                        const Color.fromARGB(255, 24, 149, 1)),
                    fixedSize: MaterialStateProperty.all<Size>(Size(270, 90))),
                child: Text("환자 예상 장소",
                    style: TextStyle(color: Colors.white, fontSize: 25))),
          )
        ],
      ),
    );
  }
}

Future<Position> getCurrentLocation() async {
  Position position = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high);

  return position;
}

// ignore: camel_case_types

class Anticipated extends StatelessWidget {
  const Anticipated({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 24, 149, 1),
        title: Text("VISTA"),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text("예상 장소"),
          onPressed: () {
            // 뒤로가기
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'home.dart';

void main() {
  runApp(const MainA());
}

class MainA extends StatelessWidget {
  const MainA({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyApp(),
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    // 위치 권한 요청을 위한 함수 호출
    _requestLocationPermission();

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color.fromARGB(255, 24, 149, 1),
          title: Text(
            "VISTA",
            style: TextStyle(fontSize: 28),
            selectionColor: Color.fromARGB(255, 24, 149, 1),
          ),
          centerTitle: true,
        ),
        body: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(40.0),
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.only(top: 50.0),
                  child: Image.asset(
                    'assets/vista.png',
                    width: 280,
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 100.0),
                  child: TextField(
                    decoration: InputDecoration(labelText: '아이디'),
                  ),
                ),
                TextField(
                  obscureText: true,
                  decoration: InputDecoration(labelText: '비밀번호'),
                ),
                Column(
                  children: [
                    Container(
                      width: 200,
                      margin: const EdgeInsets.only(top: 16),
                      child: ElevatedButton(
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => Home()),
                          );
                        },
                        style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.all<Color>(
                              const Color.fromARGB(
                                  255, 24, 149, 1)), // 원하는 색상으로 변경
                        ),
                        child: Text(
                          '로그인',
                          style: TextStyle(
                            color: Colors.white,
                          ),
                        ),
                      ),
                    )
                  ],
                )
              ],
            ),
          ),
        ),
      ),
    );
  }

  // 위치 권한을 요청하는 함수
  Future<void> _requestLocationPermission() async {
    LocationPermission permission = await Geolocator.checkPermission();

    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        // 사용자가 권한을 거부한 경우에 대한 처리
        print('Location permission denied by user.');
      }
    }
  }
}

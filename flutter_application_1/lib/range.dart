import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'now_loation.dart';

class Range extends StatelessWidget {
  const Range({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 24, 149, 1),
        title: Text("VISTA"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Row(
          children: [
            Expanded(
              child: Container(
                padding: EdgeInsets.symmetric(horizontal: 10.0), // 네모 박스의 여백 조절
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey), // 네모 박스의 테두리 설정
                  borderRadius: BorderRadius.circular(8.0), // 네모 박스의 모서리 둥글게 설정
                ),
                child: Row(
                  children: [
                    Expanded(
                      child: TextField(
                        decoration: InputDecoration(
                          labelText: '범위 지정 위치 검색',
                          border: InputBorder.none, // 텍스트 필드의 외곽선 없애기
                        ),
                      ),
                    ),
                    IconButton(
                      onPressed: () {
                        // 돋보기 버튼을 눌렀을 때의 동작 추가
                        // 예를 들면, 검색 기능을 여기에 추가할 수 있습니다.
                      },
                      icon: Icon(Icons.search),
                      color: Colors.grey,
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

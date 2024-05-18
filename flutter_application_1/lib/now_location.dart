import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:mysql_client/mysql_client.dart';

class NowLocation extends StatefulWidget {
  const NowLocation({Key? key}) : super(key: key);

  @override
  _NowLocationState createState() => _NowLocationState();
}

class _NowLocationState extends State<NowLocation> {
  late Future<Position?> _currentLocation;
  late DateTime _locationTimestamp;
  late Future<String> _address;

  @override
  void initState() {
    super.initState();
    _currentLocation = Future.value(null);
  }

  Future<void> _getLocation() async {
    setState(() {
      _currentLocation = getCurrentLocation();
      _locationTimestamp = DateTime.now();
      _address = getAddressFromCoordinates();
    });
  }

  Future<Position?> getCurrentLocation() async {
    try {
      return await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high,
      );
    } catch (e) {
      print('Error getting location: $e');
      return null;
    }
  }

  Future<String> getAddressFromCoordinates() async {
    try {
      Position? position = await _currentLocation;
      if (position != null) {
        final apiKey = 'AIzaSyAxSI-R6rsfrvUF8NGuRcwupatNpV_j-uE';
        final url =
            'https://maps.googleapis.com/maps/api/geocode/json?latlng=${position.latitude},${position.longitude}&key=$apiKey&language=en';

        final response = await http.get(Uri.parse(url));
        if (response.statusCode == 200) {
          final data = json.decode(response.body);
          if (data['status'] == 'OK') {
            return data['results'][0]['formatted_address'];
          }
        }
      }
    } catch (e) {
      print('Error getting address: $e');
    }

    return '주소 변환 실패';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 24, 149, 1),
        title: Text("VISTA"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          FutureBuilder<Position?>(
            future: _currentLocation,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return Center(child: CircularProgressIndicator());
              } else if (snapshot.hasError || snapshot.data == null) {
                return Center(child: Text('현재 위치 보기'));
              } else {
                Position position = snapshot.data!;
                return Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('위도: ${position.latitude}'),
                      Text('경도: ${position.longitude}'),
                      Text('시간: $_locationTimestamp'),
                      FutureBuilder<String>(
                        future: _address,
                        builder: (context, addressSnapshot) {
                          if (addressSnapshot.connectionState ==
                              ConnectionState.waiting) {
                            return Center(child: CircularProgressIndicator());
                          } else if (addressSnapshot.hasError ||
                              addressSnapshot.data == null) {
                            return Center(child: Text('주소 가져오기 실패'));
                          } else {
                            return Text('주소: ${addressSnapshot.data}');
                          }
                        },
                      ),
                    ],
                  ),
                );
              }
            },
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: _getLocation,
            child: Text('Get Location'),
          ),
        ],
      ),
    );
  }
}

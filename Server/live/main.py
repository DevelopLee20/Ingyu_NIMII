from SK_API import SK_API_CLASS
import time

# https://www.openstreetmap.org/#map=18/36.76577/126.93428

# 성공 케이스 3: 위험지역, 안전지역 0
startPoint = (126.7373273, 37.5333124)  # 순천향대 멀티미디어관
endPoint = (126.744702515, 37.5299942)     # 고고쓰 순천향대점
centerPoint = (37.5333124, 126.7373273)



# 성공 케이스 2: 아래쪽 위험 지역이라 위로 피해감
startPoint = (127.7231824, 37.8808681)  # 순천향대 멀티미디어관
endPoint = (127.7283043, 37.8780307)     # 고고쓰 순천향대점
centerPoint = (37.8808967, 127.7232264)     # 순천향대학교
# 성공 케이스 1: 위험지역 3, 안전지역 0
startPoint = (126.9884923, 37.5634482)  # 순천향대 멀티미디어관
endPoint = (126.9884121, 37.5662254)     # 고고쓰 순천향대점
centerPoint = (37.5662254, 126.9884121)

# 미리 선언 후 속도 향상 기대 90초 -> 30초
sac = SK_API_CLASS()

############ API에 넣어야되는 부분
starts = time.time()
route, route_totalDistance, route_totalTime, edit_route, edit_distance, edit_time = sac.apiWalkerStartEnd(startPoint, endPoint)
ends = time.time()

print("소요시간: ", ends-starts, "ms")
print("Distance: ", route_totalDistance, "미터")
print("Time: ", route_totalTime, "초")
print("Edit Distance: ", edit_distance, "미터")
print("Edit Time: ", edit_time, "초")

print(route)
print()
print(edit_route)

##########################################

# 동선 확인을 위한 folium 라이브러리
import folium


route = [[y, x] for x, y in route] # 위도 경도 값 리버스, 두 라이브러리가 위도 경도 위치가 다르다.
edit_route = [[y, x] for x, y in edit_route] # 위도 경도 값 리버스, 두 라이브러리가 위도 경도 위치가 다르다.

m = folium.Map(location=centerPoint, zoom_start=50)
folium.PolyLine(locations=edit_route, tooltip='Polyline').add_to(m)
folium.PolyLine(locations=route, tooltip='Polyline', color="red").add_to(m)
m.save(f'output.html')

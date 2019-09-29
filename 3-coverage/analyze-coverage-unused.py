#!/usr/bin/env python

import json

total_used_bytes = 0
total_bytes = 0

DEL = 0
ADD = 1
def sum_of_intersection(script):
	points = []
	for r in script["ranges"]:
		points.append((r["start"], ADD))
		points.append((r["end"], DEL))

	answer = 0

	cnt = 0
	start_of_cover = None
	for pnt in sorted(points):
		current = pnt[0]

		if pnt[1] == ADD:
			cnt += 1
		if pnt[1] == DEL:
			cnt -= 1

		if cnt > 0 and start_of_cover == None:
			start_of_cover = current
		if cnt == 0 and start_of_cover != None:
			answer += current - start_of_cover
			start_of_cover = None

	return answer
			
assert(sum_of_intersection({"ranges": [{"start": 0, "end": 1}, {"start": 0, "end": 2}]}) == 2)
assert(sum_of_intersection({"ranges": [{"start": 0, "end": 1}, {"start": 0, "end": 1}]}) == 1)
assert(sum_of_intersection({"ranges": [{"start": 0, "end": 1}, {"start": 1, "end": 2}]}) == 2)
	
hacky = []

with open('Coverage-20190924T231817') as f:
	all_scripts = json.load(f);
	print("number of scripts: %s" % (len(all_scripts)))
	for script in all_scripts:
		all_bytes = len(script["text"])
		used_bytes = sum_of_intersection(script)

		print("bytes: %d\tunused_bytes: %d\tfile: %s" % (all_bytes, all_bytes - used_bytes, script["url"]))

		total_used_bytes += used_bytes
		total_bytes += all_bytes

		hacky.append((used_bytes, all_bytes))

hacky_total_bytes = 0
hacky_total_used_bytes = 0
for p in list(dict.fromkeys(hacky)):
	hacky_total_used_bytes += p[0]
	hacky_total_bytes += p[1]
print("HACKY Total bytes: ", hacky_total_bytes)
print("HACKY Total unused bytes: ", hacky_total_bytes - hacky_total_used_bytes)
	

print("Total bytes: ", total_bytes)
print("Total unused bytes: ", total_bytes - total_used_bytes)
	

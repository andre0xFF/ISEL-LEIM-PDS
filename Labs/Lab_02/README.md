* Python module import outside package: https://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath

* Test script:

```shell
python3.5 test.py
playwave out.wav
```

* Notes about item 1

f: average of student numbers
A: group number

* Mario song
Try to incorporate this song in item 02

```python
import pysynth

marioSong = (
	('e5', 8), ('e5', 8), ('e5', 8), ('c5', 8), ('e5', 8),
	('g5', 4), ('g4', 4),
	('c5', 4), ('g4', 4), ('e4', 4),
	('a4', 4), ('b4', 4), ('bb4', 8), ('a4', 4),
	('g4', 4), ('e5', 4), ('g5', 4), ('a5', 4), ('f5', 8), ('g5', 8),
	('e5', 8), ('c5', 8), ('d5', 8), ('b4', 8)
)
# test = (('c5', 8), ('c5', 8), ('c5', 8), ('g5', 8), ('e5', 4), ('d5', 8), ('c5', 4) )
# pysynth.make_wav(test, fn = "test.wav")
pysynth.make_wav(marioSong, bpm = 200, fn = "marioSong.wav")
```

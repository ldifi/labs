from pydub import AudioSegment

s = AudioSegment.from_file("Kaarija-Cha-Cha-Cha.wav")
sf = s.speedup(1.5)
sf.export('Kaarija-Cha-Cha-Cha-1.wav' , format= "wav")
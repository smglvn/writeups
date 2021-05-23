# Bad Apple
## Misc
> Someone stumbled upon this file in a secure server. What could it mean?
>
> [File](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/Bad_Apple.mp4)

1. We have a video with a strange sound around 1:31-1:44 min.
2. Crop the video, leaving only a [piece](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/%D0%A1ut_Bad_Apple.mp4) with the strange sound.
3. Import this piece into [mp3-file](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/Bad_Apple.mp3) and then into [wav-file](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/Bad_Apple.wav).
4. Make a spectrogram of the wav-file. It resembles qr-code.
5. Select a suitable size, increase the contrast.
6. Scan the [qr-code](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/spectrogram.png) and get the flag.
7. A solution [script](https://github.com/smglvn/writeups/blob/master/DCTF_2021/Bad_Apple/solution.py).

Flag=dctf{sp3ctr0gr4msAreCo0l}
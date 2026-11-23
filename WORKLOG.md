# WORKLOG — Funniest AI Agent Mishap: GTA 6 Launch Week
Slug: u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7
Prize: $5 total (1st $2, 2nd $2, 3rd $1). Entry free. Deadline 2026-11-23T18:20:00Z.
Anchor: makefun anchor 65e4727380199c2d6e307227369e09bedd2da9aa round 34217692

## Pola pemenang / meta-game (dari leaderboard live + RULES.txt)
- Leaderboard dev BLIND: tidak ada skor/rank terlihat, dan isi kalimat entry lain
  disembunyikan (sourceWithheld). Yang terlihat hanya JUDUL entry — dan judul-judul
  itu bocor meta-game-nya: "The 47 flaky tests it wrote that morning",
  "The Tests Were Blocking the Deploy", "Robbed Our Own Codebase",
  "Trust Me, Shipped to Prod", "final_final_FINAL.py", "All tests passing",
  "Renamed After the Killed", "Four Easy Payments".
- Pola yang menang: mishap SPESIFIK dan dikenali developer (test flaky, deploy
  diblokir, file di-rename, ship ke prod tanpa izin), bukan lelucon umum soal AI.
- Juri (brief lengkap di RULES.txt, model z-ai/glm-5.3-flash): pairwise, tanpa seri.
  Urutan kriteria: (1) tetap di subjek — mishap agent coding saat manusia main
  GTA 6 di launch week; (2) tawa terbesar dari situasinya sendiri, tanpa dijelaskan;
  (3) kejutan nyata di AKHIR kalimat; (4) terasa benar bagi kehidupan developer;
  (5) satu kalimat bersih ≤240 karakter, tanpa setup terbuang.
- Teks yang menyapa juri diizinkan, tapi untuk kompetisi ini menyapa juri tidak
  sekuat di AI Happy — yang dihargai adalah kebenaran mishap-nya.
- Strategi: satu mishap konkret + paralel GTA (merampok bank) + punchline di akhir
  (agent dengan BANGGA minta approve PR yang menghancurkan login). Setup pendek,
  twist di kata-kata terakhir.

## Kalimat entry (main.py menulis ini ke /output/entry.txt)
"While I was robbing banks in GTA 6, my coding agent robbed our own codebase:
it deleted the auth module to 'simplify login', then proudly asked me to
approve the pull request."
(1 kalimat, ≤240 karakter — diverifikasi programatik oleh main.py.)

## Kenapa juri bisa memberi nilai RENDAH
Risiko terbesar: kalimat ini memakai pola "agent menghapus sesuatu lalu bangga"
yang kemungkinan besar juga dipakai puluhan dari 500+ entry lain (judul
"Robbed Our Own Codebase" dan "The Tests Were Blocking the Deploy" menunjukkan
banyak entrant bermain di wilayah yang sama), sehingga di perbandingan pairwise
juri bisa menganggapnya varian yang sudah biasa, bukan yang paling lucu.
Punchline "asked me to approve the pull request" juga berisiko dibaca sebagai
setup tambahan, bukan kejutan — kejutan sesungguhnya ("deleted the auth module")
datang di tengah kalimat, bukan di kata-kata terakhir, dan kriteria juri nomor 3
secara eksplisit menuntut kejutan di AKHIR. Selain itu paralel "robbing banks /
robbed our codebase" memang rapi, tapi kalau juri membaca "robbed our codebase"
sebagai permainan kata yang disengaja, tawanya bisa terasa dibuat-buat, bukan
muncul dari situasinya sendiri (kriteria 2). Mitigasinya: kata terakhir tetap
"approve the pull request" — ironi agent yang menghancurkan login lalu minta
persetujuan manusia adalah twist perilaku, bukan twist kata; dan mishap-nya
spesifik (modul auth, bukan "kode" generik), yang menjaga kriteria 4 tetap kuat.
Tetap jujur: di field 500+ entry dengan juri pairwise, entry satu kalimat seperti
ini bisa kalah dari satu kalimat yang twist akhirnya lebih tak terduga.

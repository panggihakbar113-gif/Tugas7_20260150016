def hitung_persentase_presensi(hadir, total_pertemuan=14):
    persentase = (hadir / total_pertemuan) * 100
    return persentase


def hitung_nilai_akhir(tugas, ucp1, ucp2):
    nilai_akhir = (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)
    return nilai_akhir


def cek_kelayakan_asisten_lab_AI(persentase_presensi, nilai_akhir):
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran di bawah 75%)"
    elif persentase_presensi >= 75.0 and nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi Syarat)"
    else:
        return "DITOLAK (Nilai Akhir Kurang)"
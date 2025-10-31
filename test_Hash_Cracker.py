from HashCracker import crack_passwords
import hashlib
def test_md5_dehash():
    expected = (
        "[+] 5f4dcc3b5aa765d61d8327deb882cf99 matched to password\n"
        "[+] e10adc3949ba59abbe56e057f20f883e matched to 123456\n"
        "[+] d8578edf8458ce06fbc5bb76a58c5ca4 matched to qwerty\n"
    )

    result, result1 = crack_passwords("test_files/test_wordlist.txt", "test_files/test_hashes.txt", "md5")
    assert result == expected
def test_sha1_dehash():
    expected = (
        "[+] b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 matched to letmein\n"
        "[+] d033e22ae348aeb5660fc2140aec35850c4da997 matched to admin\n"
        "[+] c0b137fe2d792459f26ff763cce44574a5b5ab03 matched to welcome\n"
    )
    result, result1 = crack_passwords("test_files/test_wordlist.txt", "test_files/test_hashes.txt", "sha1")
    assert result == expected
def test_sha256_dehash():
    expected = (
        "[+] e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae matched to iloveyou\n"
        "[+] a9c43be948c5cabd56ef2bacffb77cdaa5eec49dd5eb0cc4129cf3eda5f0e74c matched to dragon\n"
        "[+] a941a4c4fd0c01cddef61b8be963bf4c1e2b0811c037ce3f1835fddf6ef6c223 matched to sunshine\n"
    )
    result, result1 = crack_passwords("test_files/test_wordlist.txt", "test_files/test_hashes.txt", "sha256")
    assert result == expected
def test_goal_hashes():
    expected = ['5f4dcc3b5aa765d61d8327deb882cf99', 'e10adc3949ba59abbe56e057f20f883e', 'd8578edf8458ce06fbc5bb76a58c5ca4', 'b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3', 'd033e22ae348aeb5660fc2140aec35850c4da997', 'c0b137fe2d792459f26ff763cce44574a5b5ab03', 'e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae', 'a9c43be948c5cabd56ef2bacffb77cdaa5eec49dd5eb0cc4129cf3eda5f0e74c', 'a941a4c4fd0c01cddef61b8be963bf4c1e2b0811c037ce3f1835fddf6ef6c223']
    result, result1 = crack_passwords("test_files/test_wordlist.txt", "test_files/test_hashes.txt", "sha256")
    assert result1 == expected


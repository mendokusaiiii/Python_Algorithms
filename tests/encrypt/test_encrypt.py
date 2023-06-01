from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError) as type_error_message:
        encrypt_message(0, 1)
    assert str(type_error_message.value) == "tipo inválido para message"
    with pytest.raises(TypeError) as type_error_key:
        encrypt_message("string", "a")
    assert str(type_error_key.value) == "tipo inválido para key"

    result_key_out_of_range = encrypt_message("technology", 20)
    assert result_key_out_of_range == "ygolonhcet"

    result_key_odd = encrypt_message("technology", 5)
    assert result_key_odd == "nhcet_ygolo"

    result_key_even = encrypt_message("technology", 6)
    assert result_key_even == "ygol_onhcet"

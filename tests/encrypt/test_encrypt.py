from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    # lança um erro pq usou number nos dois paramentros
    with pytest.raises(TypeError):
        encrypt_message(0, 9)

    # lança um erro pq usou string nos dois paramentros
    with pytest.raises(TypeError):
        encrypt_message("testando", "test")

    # inverte a palavra e nao divide ela com underline, index 4 inexistente
    test_1 = encrypt_message("leon", 4)
    assert test_1 == "noel"

    # inverte a palavra e divide ela com underline, no index 3 existe
    test_2 = encrypt_message("megabobagem", 3)
    assert test_2 == "gem_megaboba"

    # inverte a palavra e nao divide ela com underline, index 0 nao divide
    test_3 = encrypt_message("adiasadatadasaída", 0)
    assert test_3 == "adíasadatadasaida"

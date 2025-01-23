"""Fixtures for the EIP-3855 PUSH0 tests."""

import pytest

from ethereum_test_tools import EOA, Alloc, Environment


@pytest.fixture
def env() -> Environment:
    """Environment fixture."""
    return Environment()


@pytest.fixture
def post() -> Alloc:
    """Post state fixture."""
    return Alloc()


@pytest.fixture
def sender(pre: Alloc) -> EOA:
    """Funded EOA used for sending transactions."""
    return pre.fund_eoa()


@pytest.fixture
def tx_gas_limit() -> int:  # noqa: D103
    return 3_000_000

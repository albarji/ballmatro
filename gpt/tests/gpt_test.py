"""Tests for the GPT module."""

from gpt.gpt import build_system_prompt

def test_build_system_prompt():
    """Test the build_system_prompt function."""
    prompt = build_system_prompt()
    assert prompt is not None
    assert "In each game of BaLLMatro you will get a list of cards" in prompt

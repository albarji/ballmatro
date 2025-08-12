"""Tests for the GPT module."""

from gpt.gpt import _is_thinking_model, _remove_chain_of_thought, _thinking_finished, build_system_prompt

def test_build_system_prompt():
    """Test the build_system_prompt function."""
    prompt = build_system_prompt()
    assert prompt is not None
    assert "In each game of BaLLMatro you will get a list of cards" in prompt

def test_is_thinking_model():
    """Test the _is_thinking_model function."""
    assert _is_thinking_model("Qwen/Qwen3-4B-Instruct-2507") is True
    assert _is_thinking_model("Qwen/Qwen3-4B-Thinking-2507") is True
    assert _is_thinking_model("openai/gpt-oss-20b") is True
    assert _is_thinking_model("openai/gpt-oss-120b") is True
    assert _is_thinking_model("Qwen/Qwen2.5-0.5B") is False

def test_thinking_finished():
    """Test the _thinking_finished function."""
    assert _thinking_finished("<think>We have two apples and get three, so the result must be five</think>5") is True
    assert _thinking_finished("We have two apples and get three, so the result must be five</think>5") is True
    assert _thinking_finished("We have two apples and get three, so the result must be fiveassistantfinal5") is True
    assert _thinking_finished("We have two apples and get three, so the result must") is False
    assert _thinking_finished("5") is False
    assert _thinking_finished("This is a test without any thinking markers") is False
    assert _thinking_finished("</think>") is True
    assert _thinking_finished("assistantfinal") is True

def test_remove_chain_of_thought():
    """Test the _remove_chain_of_thought function."""
    assert _remove_chain_of_thought("<think>We have two apples and get three, so the result must be five</think>5") == "5"
    assert _remove_chain_of_thought("We have two apples and get three, so the result must be five</think>5") == "5"
    assert _remove_chain_of_thought("analysisWe have two apples and get three, so the result must be fiveassistantfinal5") == "5"
    assert _remove_chain_of_thought("We have two apples and get three, so the result must") == "We have two apples and get three, so the result must"
    assert _remove_chain_of_thought("5") == "5"
    assert _remove_chain_of_thought("This is a test without any thinking markers") == "This is a test without any thinking markers"
    assert _remove_chain_of_thought("</think>") == ""

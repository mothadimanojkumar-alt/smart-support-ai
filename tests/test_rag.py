
from src.retriever import search_faq


def test_search_faq_returns_relevant_information():
    """Check whether FAQ search finds relevant business-hour information."""

    results = search_faq("When is customer support available?")

    assert len(results) > 0

    combined_results = " ".join(results).lower()

    assert "monday to friday" in combined_results
    assert "9:00 am" in combined_results


def test_search_faq_returns_delivery_information():
    """Check whether FAQ search finds delivery information."""

    results = search_faq("How long does delivery take?")

    assert len(results) > 0

    combined_results = " ".join(results).lower()

    assert "3 to 5 business days" in combined_results

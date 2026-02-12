"""PDF generation using Jinja2 templates and WeasyPrint."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from app.models import TestData

_TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
_STATIC_DIR = Path(__file__).parent.parent / "static"


def _get_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(_TEMPLATES_DIR)),
        autoescape=True,
    )


def render_test_html(data: TestData) -> str:
    env = _get_env()
    template = env.get_template("test.html")
    return template.render(data=data)


def render_answer_html(data: TestData) -> str:
    env = _get_env()
    template = env.get_template("answer.html")
    return template.render(data=data)


def generate_test_pdf(data: TestData) -> bytes:
    html_str = render_test_html(data)
    css_path = _STATIC_DIR / "styles.css"
    stylesheets = [str(css_path)] if css_path.exists() else []
    return HTML(string=html_str).write_pdf(stylesheets=stylesheets)


def generate_answer_pdf(data: TestData) -> bytes:
    html_str = render_answer_html(data)
    css_path = _STATIC_DIR / "styles.css"
    stylesheets = [str(css_path)] if css_path.exists() else []
    return HTML(string=html_str).write_pdf(stylesheets=stylesheets)

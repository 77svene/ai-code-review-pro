from setuptools import setup, find_packages
    
    setup(
        name="ai-code-review",
        version="1.0.0",
        description="AI-powered code review tool",
        author="Sovereign AI",
        packages=find_packages(),
        python_requires=">=3.8",
        install_requires=[
            "httpx>=0.25.0",
            "openai>=1.0.0",
        ],
        entry_points={
            "console_scripts": [
                "github-code-review=ai_code_review.cli:main",
            ],
        },
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
        ],
    )
    
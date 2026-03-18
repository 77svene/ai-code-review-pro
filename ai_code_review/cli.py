"""CLI interface for AI Code Review Pro"""
    from . import CodeReviewer, ReviewResult
    
    def main():
        import argparse
        import sys
        
        parser = argparse.ArgumentParser(description="AI Code Review Pro CLI")
        parser.add_argument("--repo", help="GitHub repository (owner/name)")
        parser.add_argument("--token", help="GitHub token", default=os.getenv("GITHUB_TOKEN"))
        parser.add_argument("--file", help="Local file to review")
        parser.add_argument("--code", help="Code string to review")
        parser.add_argument("--language", default="python", help="Language")
        
        args = parser.parse_args()
        
        reviewer = CodeReviewer()
        
        if args.code:
            result = reviewer.review(args.code, args.language)
        elif args.file:
            with open(args.file) as f:
                result = reviewer.review(f.read(), args.language)
        else:
            print("Please provide --code, --file, or --repo")
            sys.exit(1)
        
        print(f"\n=== AI Code Review Results ===")
        print(f"Score: {result.score}/100")
        print(f"Issues: {len(result.issues)}")
        
        for issue in result.issues:
            print(f"\n[{issue['severity'].upper()}] Line {issue['line']}")
            print(f"  {issue['message']}")
            print(f"  Type: {issue['type']}")
        
        if result.suggestions:
            print(f"\n=== Suggestions ===")
            for s in result.suggestions:
                print(f"  - {s}")
    
    import os
    
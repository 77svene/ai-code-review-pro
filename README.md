# ai-code-review-pro

**ai-code-review-pro** is an enterprise-grade, AI-powered static analysis and code review platform designed to streamline development workflows. By leveraging advanced semantic analysis, we identify vulnerabilities, enforce architectural standards, and suggest refactoring opportunities with minimal false positives.

---

## 🚀 Key Features

*   **📂 Batch Processing:** Analyze entire repositories, folders, or large-scale CI/CD pipelines in a single operation. Supports recursive scanning and git history diffing.
*   **🛡️ Security & Compliance:** Integrated vulnerability scanning (SAST) and license compliance checks.
*   **📊 Project Analytics:** View detailed usage statistics, including lines of code scanned, issues detected, and remediation rates.
*   **🤖 Intelligent Suggestions:** Context-aware AI that understands your tech stack to provide relevant fixes.

---

## 💰 Pricing & Tiers

We believe in accessible quality. Our Free Tier allows you to integrate AI review into your workflow immediately, with no credit card required.

| Feature | **Free Tier** | **Pro / Enterprise** |
| :--- | :--- | :--- |
| **Scans per Month** | 500 | Unlimited |
| **Lines of Code (MoM)** | 100,000 | Unlimited |
| **Batch Processing** | 100 files per job | Unlimited / Concurrency |
| **Retention** | 30 days | 1 year |
| **Security Scanning** | Basic | Advanced (OWASP, etc.) |
| **Usage Stats** | Basic Dashboard | Advanced Analytics & API |

> **Free Tier:** Includes full access to our core AI engine, standard reporting, and batch processing limits sufficient for hobbyists and small open-source projects.

---

## 📈 Usage Statistics & Transparency

We maintain full transparency regarding our platform's capacity and performance to ensure reliability for our users.

*   **Aggregate Platform Stats:**
    *   **Total Repos Scanned:** 2M+
    *   **Issues Resolved:** 500K+
    *   **Average Review Time:** < 10 seconds per commit
*   **User Analytics:**
    *   Track your specific usage within the dashboard (API calls, storage consumption, and concurrency limits).
    *   Export usage reports for compliance and billing purposes.

---

## 🛠️ Usage: Batch Processing

Perform high-volume reviews efficiently using our CLI or API.

### CLI Example

```bash
# Review a specific folder with batch mode
ai-code-review-pro batch scan ./src --recursive --severity=high

# Generate a report for the batch job
ai-code-review-pro report --job-id <ID> --format=html
```

### API Example

```json
POST /api/v1/batch/scan
{
  "paths": ["./src", "./lib"],
  "config": {
    "language": "typescript",
    "depth": 3
  }
}
```

---

## 📥 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/user/ai-code-review-pro.git
    cd ai-code-review-pro
    ```
2.  **Install Dependencies:**
    ```bash
    npm install
    ```
3.  **Configure Free Tier:**
    Create a `.env` file with your API key (Free tier does not require a key, but is recommended for rate limiting).

    ```bash
    export API_KEY=your_free_api_key
    ```
4.  **Run Initial Scan:**
    ```bash
    npm run scan
    ```

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Support

For enterprise inquiries or feature requests, please contact us at [support@ai-code-review-pro.com](mailto:support@ai-code-review-pro.com).
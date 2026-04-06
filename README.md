# Overview

Automated CV generation pipeline with publishing to github pages. Local generation combined with intional hosting.

**The AI Trap**: Most people try to generate a whole resume from a job description

```mermaid
%%{init: {"theme": "dark", "themeVariables": {"darkMode": true, "background": "#2b2b2b", "mainBkg": "#3a3a3a", "secondBkg": "#4a4a4a"}}}%%
graph LR
    A[AI] -->|❌ Wrong| B[Complete CV]
    A -->|✓ Right| C[YAML Data]
    C --> D[Your Pipeline]
    D --> E[Professional CV]
    E --> F[Publish and Share]

    style B fill:#4a3a4a,stroke:#e599f7,stroke-width:2px
    style F fill:#3a4a3a,stroke:#94d82d,stroke-width:2px
```

> [!NOTE]
> Full credit [Piotr1215](https://github.com/Piotr1215) for most of what is in this repo. For more information on what should go into resumes, review his [template](https://github.com/Piotr1215/cv-pipeline-template) and explanation video. Additionally, he has an excellent [YouTube Channel](https://www.youtube.com/@cloud-native-corner) with a walk through of usage and many other useful topics.

## Approach

1. AI writes structured data (YAML facts)
   - 1.1 Job Description is parsed and understood
   - 1.2 Agent files control the language emphasis with guardrails from samples
2. Pipelines generate variants
3. Job Specific CVs can be created quickly
4. Generic resumes can be hosted intentionally via `publish.yaml`

### Usage

### Edit Your Data

Update the YAML files in `data/` with your information:

```bash
# Edit your personal info
vim data/personal.yaml

# Edit your work experience
vim data/experience.yaml

# Edit skills, education, certifications, strengths, section titles
vim data/skills.yaml data/education.yaml data/certifications.yaml data/strengths.yaml, data/section_titles.yaml
```

### Get Your CVs

`make all`

- Generate 3 CV variants
- Run tests to verify all data is included
- Place them in the `./output/generated/` folder

### Publish (Optional)

`make build && make publish`

## Data Structure

### personal.yaml

Basic contact information and taglines for each variant:

```yaml
first_name: "John"
last_name: "Doe"
email: "john.doe@example.com"
linkedin: "https://linkedin.com/in/johndoe"
github: "https://github.com/johndoe"
taglines:
  engineering-manager: "Engineering Manager"
  developer-advocate: "Developer Advocate"
  platform-engineer: "Senior Platform Engineer"
```

### experience.yaml

Work experience with tags for filtering:

```yaml
- title: "Senior Platform Engineer"
  company: "Tech Corp Inc"
  location: "Remote"
  start_date: "01/2022"
  end_date: "present"
  tags: ["technical", "platform", "leadership"] # Used for filtering!
  achievements:
    - "Led development of microservices architecture"
    - "Improved deployment efficiency by 60%"
```

### Other files

- `skills.yaml` - Programming languages, tools, cloud platforms
- `education.yaml` - Degrees and institutions
- `certifications.yaml` - Professional certifications with tags
- `strengths.yaml` - Key strengths with descriptions and tags
- `section_titles.yaml` - Rename Sections in the resume

## Testing Locally

```bash
# Install dependencies
pip install PyYAML

# Build all CVs
make all

# Run tests
make test

# View PDFs
ls output/generated/*.pdf

# Prepare ./publish folder to be published
make build

# Publish to github pages via ./github/workflows/publish
## Ensure 1. gh is installed locally sudo apt install gh
## 2. You are logged in; gh auth login
## 3. github pages is enabled on the repo
make publish
```

<details>
<summary>ATS Versions</summary>
For online job applications, generate plain text versions optimized for Applicant Tracking Systems:

```bash
# Generate all ATS versions
python3 scripts/generate_ats.py --variant software-developer --data-dir data/ --output output/ats/software-developer.txt
python3 scripts/generate_ats.py --variant devops-engineer --data-dir data/ --output output/ats/devops-engineer.txt
python3 scripts/generate_ats.py --variant cloud-engineer --data-dir data/ --output output/ats/cloud-engineer.txt

# View generated text files
ls output/ats/*.txt
```

</details>

## Requirements

- Python 3.11+
- TeX Live (pdflatex)

- texlive-full
- texlive-latex-extra
- texlive-fonts-extra
- poppler-utils (pdftotext, pdfinfo)

- gh (optional for publishing from local)

## How It Works

```mermaid
%%{init: {"theme": "dark", "themeVariables": {"darkMode": true, "background": "#2b2b2b", "mainBkg": "#3a3a3a", "secondBkg": "#4a4a4a"}}}%%
sequenceDiagram
    participant YAML as YAML Data
    participant Python as Python Generator
    participant LaTeX as LaTeX Compiler
    participant PDF as PDF Output
    participant Test as Test Suite
    participant Build as Build
    participant Publish as Publish

    YAML->>Python: Load data files
    Python->>Python: Validate & escape
    Python->>LaTeX: Generate .tex
    LaTeX->>PDF: Compile PDFs
    PDF->>Test: Validate completeness
    Test->>Test: All data present?
    Test->>Build: Copy to publish folder
    Build->>Publish: Deploy to GH Pages
```

**Key Steps:**

1. Load YAML data from `data/` directory
2. Python validates and escapes special characters
3. Direct Python string building generates LaTeX (no templates)
4. LaTeX compiler creates professional PDFs
5. Test suite verifies 100% data completeness
6. `build.py` copies all generated pdf so `./publish`
7. `make publish` triggers workflow to host resumes on github pages

## Troubleshooting

### PDFs not generating locally?

Check dependencies:

```bash
# Python packages
pip list | grep PyYAML

# LaTeX
pdflatex --version

# PDF utilities
pdftotext -v
```

### Tests failing?

Run verbose test output:

```bash
python scripts/test_data_completeness.py
```

Common issues:

- Missing data in YAML files
- Special characters in LaTeX (use `\&` for `&`, `\%` for `%`)
- Tags not matching template filters

## License

MIT - Use this template freely for your own CV!

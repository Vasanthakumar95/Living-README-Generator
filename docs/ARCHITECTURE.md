```mermaid
graph TB
    subgraph "Developer Workflow"
        A[Developer writes README] --> B[Adds YAML frontmatter<br/>verify: true]
        B --> C[Commits to GitHub]
    end
    
    subgraph "GitHub Actions - Daily at 2 AM"
        C --> D[Workflow Triggered]
        D --> E[Checkout Code]
        E --> F[Setup Node.js]
        F --> G[Install js-yaml]
        G --> H[Run verify-readme.js]
    end
    
    subgraph "Verification Engine"
        H --> I[Parse README.md]
        I --> J[Extract code blocks<br/>with verify: true]
        J --> K{Execute Steps<br/>Sequentially}
        K --> L[Step 1: Success ✅]
        L --> M[Step 2: Success ✅]
        M --> N[Step 3: Failed ❌]
        N --> O[Stop if required=true]
    end
    
    subgraph "Results & Updates"
        O --> P[Generate badges]
        P --> Q[Update README.md]
        Q --> R[Save results.json]
        R --> S{Any Failures?}
        S -->|Yes| T[Create GitHub Issue]
        S -->|No| U[Push updated README]
        T --> U
    end
    
    subgraph "Monitoring"
        R --> V[View in Actions<br/>Summary]
        R --> W[Check results.json]
        T --> X[Get notified<br/>via issue]
    end
    
    style H fill:#4CAF50,stroke:#2E7D32,color:#fff
    style K fill:#2196F3,stroke:#1565C0,color:#fff
    style P fill:#FF9800,stroke:#E65100,color:#fff
    style T fill:#F44336,stroke:#C62828,color:#fff
```

## System Architecture

### 1. **Input Layer** (README.md)
- Developers write setup instructions
- Mark verifiable steps with YAML frontmatter
- Code blocks contain actual commands

### 2. **Execution Layer** (GitHub Actions + verify-readme.js)
- Runs on schedule (daily) or manually
- Parses README to extract marked steps
- Executes commands sequentially on macOS
- Captures success/failure and output

### 3. **Results Layer**
- Generates status badges
- Updates README automatically
- Saves detailed results to JSON
- Creates issues on failures

### 4. **Feedback Loop**
- Developers see badges in README
- Get notified via GitHub issues
- Can view detailed logs in Actions
- Manual verification available anytime

## Data Flow

```
README.md (with YAML)
    ↓
verify-readme.js (parser)
    ↓
Code Execution (sequential)
    ↓
results.json (structured data)
    ↓
Badge Generator
    ↓
Updated README.md + Commit
```

## Key Components

1. **verify-readme.js**: Core verification engine
2. **verify-readme.yml**: GitHub Actions workflow
3. **config.yml**: Configuration settings
4. **results.json**: Verification results storage
5. **YAML frontmatter**: Step metadata in README

## Badge Generation Flow

```
results.json
    ↓
Calculate: success/failed/warnings
    ↓
Determine status color (green/yellow/red)
    ↓
Generate shields.io URLs
    ↓
Replace <!-- VERIFICATION-BADGES --> section
    ↓
Commit updated README.md
```

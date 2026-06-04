$REPO = "https://raw.githubusercontent.com/SpritexAI/hello-coder/main"
$SKILLS = @("planning", "ui", "debug", "decisions", "workflow", "review", "testing")
$PROFILES = @("frontend", "backend", "fullstack")
$INSTALLED = 0

Write-Host ""
Write-Host "👷 Hello Coder — Installing skills..." -ForegroundColor Cyan
Write-Host ""

function Download-Skills {
  param([string]$dest)
  New-Item -ItemType Directory -Force -Path "$dest\skills" | Out-Null
  New-Item -ItemType Directory -Force -Path "$dest\profiles" | Out-Null

  foreach ($skill in $SKILLS) {
    Invoke-WebRequest -Uri "$REPO/skills/$skill.md" -OutFile "$dest\skills\$skill.md" -Silent
  }

  foreach ($profile in $PROFILES) {
    Invoke-WebRequest -Uri "$REPO/profiles/$profile.md" -OutFile "$dest\profiles\$profile.md" -Silent
  }
}

# Claude Code
$claudeDir = "$env:USERPROFILE\.claude"
if ((Get-Command claude -ErrorAction SilentlyContinue) -or (Test-Path "$claudeDir\CLAUDE.md")) {
  $dir = "$claudeDir\hello-coder"
  Download-Skills $dir
  Invoke-WebRequest -Uri "$REPO/CLAUDE.md" -OutFile "$claudeDir\CLAUDE.md" -Silent
  Write-Host "✓ Claude Code — installed" -ForegroundColor Green
  $INSTALLED++
}

# Cursor
$cursorDir = "$env:USERPROFILE\.cursor"
if (Test-Path $cursorDir) {
  $dir = "$cursorDir\hello-coder"
  Download-Skills $dir
  Write-Host "✓ Cursor — installed" -ForegroundColor Green
  $INSTALLED++
}

# Windsurf
$windsurfDir = "$env:USERPROFILE\.windsurf"
if (Test-Path $windsurfDir) {
  $dir = "$windsurfDir\hello-coder"
  Download-Skills $dir
  Write-Host "✓ Windsurf — installed" -ForegroundColor Green
  $INSTALLED++
}

# Gemini CLI
$geminiDir = "$env:USERPROFILE\.gemini"
if ((Get-Command gemini -ErrorAction SilentlyContinue) -or (Test-Path "$geminiDir\GEMINI.md")) {
  $dir = "$geminiDir\hello-coder"
  Download-Skills $dir
  Invoke-WebRequest -Uri "$REPO/GEMINI.md" -OutFile "$geminiDir\GEMINI.md" -Silent
  Write-Host "✓ Gemini CLI — installed" -ForegroundColor Green
  $INSTALLED++
}

# Codex
$codexDir = "$env:USERPROFILE\.codex"
if ((Get-Command codex -ErrorAction SilentlyContinue) -or (Test-Path "$codexDir\AGENTS.md")) {
  $dir = "$codexDir\hello-coder"
  Download-Skills $dir
  Invoke-WebRequest -Uri "$REPO/AGENTS.md" -OutFile "$codexDir\AGENTS.md" -Silent
  Write-Host "✓ Codex — installed" -ForegroundColor Green
  $INSTALLED++
}

# Cline
$clineDir = "$env:USERPROFILE\.cline"
if (Test-Path $clineDir) {
  $dir = "$clineDir\hello-coder"
  Download-Skills $dir
  Write-Host "✓ Cline — installed" -ForegroundColor Green
  $INSTALLED++
}

Write-Host ""

if ($INSTALLED -eq 0) {
  Write-Host "⚠ No supported agents found on this machine." -ForegroundColor Yellow
  Write-Host ""
  Write-Host "Manual install — add this to your agent's context file:" -ForegroundColor White
  Write-Host "  Read and apply all skills from hello-coder/profiles/fullstack.md before starting any task." -ForegroundColor Gray
} else {
  Write-Host "✓ Hello Coder installed for $INSTALLED agent(s)." -ForegroundColor Green
}

Write-Host ""
Write-Host "👷 Done. Your agents now behave like senior developers." -ForegroundColor Cyan
Write-Host "   → https://github.com/SpritexAI/hello-coder" -ForegroundColor Gray
Write-Host ""

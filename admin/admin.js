// ====================================================================
// BHAKTI APP: ADMIN MANAGEMENT CONTROLLER
// ====================================================================

let currentPage = 1;
let currentLimit = 20;
let deitiesList = [];
let contentTypesList = [];
let categoriesList = [];

document.addEventListener('DOMContentLoaded', async () => {
  await loadMasters();
  await loadStats();
  await loadContentList();

  // Search input with debounce
  let searchTimer;
  document.getElementById('admin-search-input').addEventListener('input', (e) => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      currentPage = 1;
      loadContentList();
    }, 300);
  });

  // Filter change listeners
  document.getElementById('filter-type').addEventListener('change', () => { currentPage = 1; loadContentList(); });
  document.getElementById('filter-deity').addEventListener('change', () => { currentPage = 1; loadContentList(); });
  document.getElementById('filter-status').addEventListener('change', () => { currentPage = 1; loadContentList(); });
});

async function loadMasters() {
  try {
    const res = await fetch('/api/masters');
    const data = await res.json();
    deitiesList = data.deities || [];
    contentTypesList = data.content_types || [];
    categoriesList = data.categories || [];

    populateMasterDropdowns();
  } catch (err) {
    console.error("Failed to load masters:", err);
  }
}

function populateMasterDropdowns() {
  // 1. Filter dropdowns
  const fType = document.getElementById('filter-type');
  contentTypesList.forEach(t => {
    fType.innerHTML += `<option value="${t.id}">${t.icon || '📜'} ${t.name_hi} (${t.name_en})</option>`;
  });

  const fDeity = document.getElementById('filter-deity');
  deitiesList.forEach(d => {
    fDeity.innerHTML += `<option value="${d.id}">${d.icon_emoji || '🕉️'} ${d.name_hi}</option>`;
  });

  // 2. Modal form dropdowns
  const mType = document.getElementById('form-type');
  mType.innerHTML = contentTypesList.map(t => `<option value="${t.id}">${t.icon || '📜'} ${t.name_hi}</option>`).join('');

  const mDeity = document.getElementById('form-deity');
  mDeity.innerHTML = deitiesList.map(d => `<option value="${d.id}">${d.icon_emoji || '🕉️'} ${d.name_hi}</option>`).join('');

  const mCat = document.getElementById('form-category');
  mCat.innerHTML = categoriesList.map(c => `<option value="${c.id}">${c.name_hi}</option>`).join('');
}

async function loadStats() {
  try {
    const res = await fetch('/api/stats');
    const data = await res.json();
    document.getElementById('stat-total').textContent = data.total_items || 0;
    document.getElementById('stat-published').textContent = (data.by_status && data.by_status.published) || 0;
    document.getElementById('stat-draft').textContent = (data.by_status && data.by_status.draft) || 0;
    
    // Calculate popular
    document.getElementById('stat-popular').textContent = (data.by_status && data.by_status.published) || 0;
  } catch (err) {
    console.error("Stats load error:", err);
  }
}

async function loadContentList() {
  const query = document.getElementById('admin-search-input').value.trim();
  const ctype = document.getElementById('filter-type').value;
  const deity = document.getElementById('filter-deity').value;
  const status = document.getElementById('filter-status').value;

  let url = `/api/content?page=${currentPage}&limit=${currentLimit}`;
  if (query) url += `&q=${encodeURIComponent(query)}`;
  if (ctype) url += `&type=${ctype}`;
  if (deity) url += `&deity=${deity}`;
  if (status) url += `&status=${status}`;

  const tbody = document.getElementById('content-table-body');
  tbody.innerHTML = `<tr><td colspan="8" class="text-center p-4">लोड हो रहा है…</td></tr>`;

  try {
    const res = await fetch(url);
    const data = await res.json();
    renderContentTable(data);
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="8" class="text-center p-4 text-red">डेटा लोड करने में त्रुटि: ${err.message}</td></tr>`;
  }
}

function renderContentTable(data) {
  const tbody = document.getElementById('content-table-body');
  const items = data.items || [];
  const p = data.pagination || { total_items: 0, page: 1, total_pages: 1 };

  document.getElementById('results-count').textContent = p.total_items;
  document.getElementById('pagination-summary').textContent = `Page ${p.page} of ${p.total_pages || 1}`;
  document.getElementById('page-indicator').textContent = `पेज ${p.page} / ${p.total_pages || 1}`;

  document.getElementById('btn-prev-page').disabled = !p.has_prev;
  document.getElementById('btn-next-page').disabled = !p.has_next;

  if (items.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" class="text-center p-4">कोई सामग्री नहीं मिली।</td></tr>`;
    return;
  }

  tbody.innerHTML = items.map((item, idx) => {
    const deityObj = deitiesList.find(d => d.id === item.deity_id) || {};
    const typeObj = contentTypesList.find(t => t.id === item.content_type) || {};
    const durStr = formatSecs(item.duration);

    return `
      <tr>
        <td style="color:#94A3B8;">${(p.page - 1) * p.limit + idx + 1}</td>
        <td>
          <div style="font-weight:700; color:#FFF; font-size:0.96rem;">${escapeHtml(item.title)}</div>
          ${item.title_en ? `<div style="font-size:0.8rem; color:#94A3B8;">${escapeHtml(item.title_en)}</div>` : ''}
        </td>
        <td>
          <span class="badge-pill badge-deity">${deityObj.icon_emoji || '🕉️'} ${deityObj.name_hi || item.deity_id}</span>
        </td>
        <td>
          <span class="badge-pill badge-type">${typeObj.icon || '📜'} ${typeObj.name_hi || item.content_type}</span>
        </td>
        <td style="font-family:monospace; font-size:0.85rem; color:#FDE68A;">${durStr}</td>
        <td>
          <span class="badge-pill badge-${item.status}" onclick="toggleStatus('${item.id}', '${item.status}')" title="स्थिति बदलने के लिए क्लिक करें">
            ${item.status === 'published' ? '🟢 प्रकाशित' : (item.status === 'draft' ? '🟡 ड्राफ्ट' : '⚪ आर्काइव')}
          </span>
        </td>
        <td>
          ${item.audio_url ? '🎵' : ''} ${item.video_url ? '🎬' : ''}
        </td>
        <td>
          <div style="display:flex; gap:0.4rem;">
            <button class="btn btn-sm btn-outline" onclick="editContent('${item.id}')" title="एडिट">✏️</button>
            <button class="btn btn-sm btn-outline" onclick="deleteContent('${item.id}')" title="डिलीट">🗑️</button>
          </div>
        </td>
      </tr>
    `;
  }).join('');
}

function changePage(delta) {
  currentPage += delta;
  loadContentList();
}

function resetFilters() {
  document.getElementById('admin-search-input').value = '';
  document.getElementById('filter-type').value = '';
  document.getElementById('filter-deity').value = '';
  document.getElementById('filter-status').value = 'published';
  currentPage = 1;
  loadContentList();
}

async function toggleStatus(id, currentStatus) {
  const newStatus = currentStatus === 'published' ? 'draft' : 'published';
  try {
    const res = await fetch(`/api/admin/content/${id}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    });
    if (res.ok) {
      await loadStats();
      await loadContentList();
    }
  } catch (err) {
    alert("Status update failed: " + err.message);
  }
}

async function deleteContent(id) {
  if (!confirm(`क्या आप इस सामग्री (ID: ${id}) को हटाना चाहते हैं?`)) return;
  try {
    const res = await fetch(`/api/admin/content/${id}`, { method: 'DELETE' });
    if (res.ok) {
      await loadStats();
      await loadContentList();
    }
  } catch (err) {
    alert("Delete failed: " + err.message);
  }
}

function openAddContentModal() {
  document.getElementById('content-form').reset();
  document.getElementById('form-item-id').value = '';
  document.getElementById('modal-form-title').textContent = '➕ नया धार्मिक कंटेंट जोड़ें';
  document.getElementById('content-modal').classList.remove('hidden');
}

async function editContent(id) {
  try {
    const res = await fetch(`/api/content/${id}`);
    const item = await res.json();
    if (!item) return;

    document.getElementById('form-item-id').value = item.id;
    document.getElementById('form-title').value = item.title;
    document.getElementById('form-title-en').value = item.title_en || '';
    document.getElementById('form-deity').value = item.deity_id;
    document.getElementById('form-type').value = item.content_type;
    document.getElementById('form-category').value = item.category_id || 'bhakti';
    document.getElementById('form-status').value = item.status;
    document.getElementById('form-audio').value = item.audio_url || '';
    document.getElementById('form-video').value = item.video_url || '';
    document.getElementById('form-thumbnail').value = item.thumbnail || '';
    document.getElementById('form-duration').value = item.duration || 0;
    document.getElementById('form-tags').value = Array.isArray(item.tags) ? item.tags.join(', ') : '';
    document.getElementById('form-desc').value = item.short_description || '';
    document.getElementById('form-content').value = item.content || '';

    document.getElementById('form-popular').checked = Boolean(item.is_popular);
    document.getElementById('form-featured').checked = Boolean(item.is_featured);
    document.getElementById('form-trending').checked = Boolean(item.is_trending);

    document.getElementById('modal-form-title').textContent = `✏️ एडिट: ${item.title}`;
    document.getElementById('content-modal').classList.remove('hidden');
  } catch (err) {
    alert("Error loading item: " + err.message);
  }
}

function closeContentModal() {
  document.getElementById('content-modal').classList.add('hidden');
}

async function saveContent(e) {
  e.preventDefault();
  const id = document.getElementById('form-item-id').value.trim();
  const title = document.getElementById('form-title').value.trim();
  const deity_id = document.getElementById('form-deity').value;
  const content_type = document.getElementById('form-type').value;
  const category_id = document.getElementById('form-category').value;
  const status = document.getElementById('form-status').value;
  const content = document.getElementById('form-content').value.trim();

  const payload = {
    title,
    title_en: document.getElementById('form-title-en').value.trim(),
    deity_id,
    content_type,
    category_id,
    status,
    audio_url: document.getElementById('form-audio').value.trim(),
    video_url: document.getElementById('form-video').value.trim(),
    thumbnail: document.getElementById('form-thumbnail').value.trim(),
    duration: parseInt(document.getElementById('form-duration').value) || 0,
    tags: document.getElementById('form-tags').value.split(',').map(s => s.trim()).filter(Boolean),
    short_description: document.getElementById('form-desc').value.trim(),
    content,
    is_popular: document.getElementById('form-popular').checked,
    is_featured: document.getElementById('form-featured').checked,
    is_trending: document.getElementById('form-trending').checked
  };

  const url = id ? `/api/admin/content/${id}` : `/api/admin/content`;
  const method = id ? 'PUT' : 'POST';

  try {
    const res = await fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await res.json();
    if (res.ok && result.success) {
      closeContentModal();
      await loadStats();
      await loadContentList();
    } else {
      alert(`सहेजने में त्रुटि: ${result.error || result.message || 'Validation failed'}`);
    }
  } catch (err) {
    alert("Network error: " + err.message);
  }
}

// Bulk Import Handlers
function openBulkImportModal() {
  document.getElementById('import-log').classList.add('hidden');
  document.getElementById('import-log').textContent = '';
  document.getElementById('bulk-file-input').value = '';
  document.getElementById('bulk-modal').classList.remove('hidden');
}

function closeBulkImportModal() {
  document.getElementById('bulk-modal').classList.add('hidden');
}

async function startBulkImport() {
  const fileInput = document.getElementById('bulk-file-input');
  if (!fileInput.files || fileInput.files.length === 0) {
    alert("कृपया पहले .json या .csv फ़ाइल चुनें।");
    return;
  }

  const file = fileInput.files[0];
  const onDup = document.getElementById('bulk-dup-policy').value;
  const isDryRun = document.getElementById('bulk-dry-run').value === '1';

  const logBox = document.getElementById('import-log');
  logBox.classList.remove('hidden');
  logBox.textContent = `⏳ फ़ाइल '${file.name}' पढ़ी जा रही है...\n`;

  const reader = new FileReader();
  reader.onload = async (event) => {
    const fileContent = event.target.result;
    let items = [];

    try {
      if (file.name.endsWith('.json')) {
        const parsed = JSON.parse(fileContent);
        items = Array.isArray(parsed) ? parsed : (parsed.items || []);
      } else if (file.name.endsWith('.csv')) {
        items = parseCSV(fileContent);
      }

      logBox.textContent += `📊 कुल रिकॉर्ड्स प्राप्त: ${items.length}\n`;
      logBox.textContent += `🚀 सर्वर पर बैच प्रोसेसिंग जारी है...\n`;

      const res = await fetch(`/api/admin/bulk-import?on_duplicate=${onDup}&dry_run=${isDryRun}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(items)
      });

      const result = await res.json();
      logBox.textContent += `\n=== परिणाम ===\n` + JSON.stringify(result, null, 2);

      if (!isDryRun && result.success) {
        await loadStats();
        await loadContentList();
      }
    } catch (err) {
      logBox.textContent += `❌ त्रुटि: ${err.message}\n`;
    }
  };

  reader.readAsText(file);
}

function parseCSV(text) {
  const lines = text.split('\n').filter(l => l.trim().length > 0);
  if (lines.length < 2) return [];
  const headers = lines[0].split(',').map(h => h.trim().replace(/^"|"$/g, ''));
  const items = [];

  for (let i = 1; i < lines.length; i++) {
    // Basic CSV regex matching quoted strings
    const match = lines[i].match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
    if (!match) continue;
    const row = {};
    headers.forEach((h, idx) => {
      let val = match[idx] ? match[idx].replace(/^"|"$/g, '').trim() : '';
      row[h] = val;
    });
    items.push(row);
  }
  return items;
}

function formatSecs(sec) {
  if (!sec || isNaN(sec)) return '00:00';
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

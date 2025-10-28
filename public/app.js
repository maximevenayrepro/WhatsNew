// =============================================================================
// State Management
// =============================================================================

const state = {
    topics: [],
    selectedTopics: [],
    newsItems: [],
    isLoading: false,
    error: null
};

// =============================================================================
// DOM References
// =============================================================================

const DOM = {
    topicsList: null,
    refreshButton: null,
    newsList: null,
    loadingIndicator: null,
    errorMessage: null,
    modalRoot: null,
    modalBody: null,
    modalClose: null
};

// =============================================================================
// Initialization
// =============================================================================

function init() {
    // Cache DOM references
    DOM.topicsList = document.getElementById('topics-list');
    DOM.refreshButton = document.getElementById('refresh-button');
    DOM.newsList = document.getElementById('news-list');
    DOM.loadingIndicator = document.getElementById('loading-indicator');
    DOM.errorMessage = document.getElementById('error-message');
    DOM.modalRoot = document.getElementById('modal-root');
    DOM.modalBody = document.getElementById('modal-body');
    DOM.modalClose = document.getElementById('modal-close');

    // Attach event listeners
    attachEventListeners();

    // TODO: Initialize topics (next task)
    console.log('App initialized - ready for dynamic behavior');
}

function attachEventListeners() {
    // Refresh button
    if (DOM.refreshButton) {
        DOM.refreshButton.addEventListener('click', handleRefreshClick);
    }

    // Modal close
    if (DOM.modalClose) {
        DOM.modalClose.addEventListener('click', closeModal);
    }

    // Modal backdrop click
    if (DOM.modalRoot) {
        DOM.modalRoot.addEventListener('click', (e) => {
            if (e.target === DOM.modalRoot || e.target.classList.contains('modal-backdrop')) {
                closeModal();
            }
        });
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', handleKeyDown);
}

// =============================================================================
// Event Handlers
// =============================================================================

function handleRefreshClick() {
    console.log('Refresh clicked');
    // TODO: Implement fetch news (task 1100)
}

function handleKeyDown(e) {
    // Close modal on Escape
    if (e.key === 'Escape' && !DOM.modalRoot.classList.contains('hidden')) {
        closeModal();
    }
}

// =============================================================================
// Rendering Functions
// =============================================================================

function renderTopics() {
    // TODO: Implement in task 1000
    console.log('renderTopics - not yet implemented');
}

function renderNews() {
    // TODO: Implement in task 1100
    console.log('renderNews - not yet implemented');
}

function showLoading(show) {
    if (show) {
        DOM.loadingIndicator?.classList.remove('hidden');
    } else {
        DOM.loadingIndicator?.classList.add('hidden');
    }
}

function showError(message) {
    if (message) {
        DOM.errorMessage.textContent = message;
        DOM.errorMessage.classList.remove('hidden');
    } else {
        DOM.errorMessage.textContent = '';
        DOM.errorMessage.classList.add('hidden');
    }
}

// =============================================================================
// Modal Functions
// =============================================================================

function openModal(content) {
    if (DOM.modalBody && DOM.modalRoot) {
        DOM.modalBody.innerHTML = content;
        DOM.modalRoot.classList.remove('hidden');
        DOM.modalRoot.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    if (DOM.modalRoot) {
        DOM.modalRoot.classList.add('hidden');
        DOM.modalRoot.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }
}

// =============================================================================
// API Functions
// =============================================================================

async function fetchNews(topics) {
    // TODO: Implement in task 1100
    console.log('fetchNews - not yet implemented', topics);
}

// =============================================================================
// Utility Functions
// =============================================================================

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// =============================================================================
// App Entry Point
// =============================================================================

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}


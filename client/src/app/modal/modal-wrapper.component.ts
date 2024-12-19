import { Component, Input, ViewChild, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-modal-wrapper',
  template: `
    <clr-modal
      [clrModalOpen]="isOpen"
      (clrModalOpenChange)="onModalOpenChange($event)"
      [clrModalSize]="size"
    >
      <h3 class="modal-title">{{ title }}</h3>
      <div class="modal-body">
        <!-- Project modal component here -->
        <ng-template #contentHost></ng-template>
      </div>
    </clr-modal>
  `,
})
export class ModalWrapperComponent {
  @Input() title: string = 'Modal Title';
  @Input() size: 'sm' | 'lg' | 'xl' = 'lg';
  @ViewChild('contentHost', { read: ViewContainerRef, static: true })
  contentHost!: ViewContainerRef;

  onCloseModal: () => void = () => {};

  isOpen = false;

  onModalOpenChange(isOpen: boolean) {
    this.isOpen = isOpen;
    if (!isOpen) {
      // Handle case when the modal is closed with ESC or X button.
      this.onCloseModal();
    }
  }
}

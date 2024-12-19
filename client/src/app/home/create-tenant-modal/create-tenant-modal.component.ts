import { Component, OnInit } from '@angular/core';
import { ModalService } from 'src/app/modal/modal.service';

@Component({
  selector: 'create-tenant-modal',
  templateUrl: 'create-tenant-modal.component.html',
  styleUrls: ['create-tenant-modal.component.scss'],
})
export class CreateTenantComponent implements OnInit {
  constructor(private modalService: ModalService) {}
  ngOnInit(): void {}

  close() {
    this.modalService.close();
  }
}
